"""Reproduce the council hotline provocation in the Long Data deck.

Pulls every record from the City of Boulder open data layer
"Emails to the City Council Hotline" (CC0), separates hotline-list traffic
from off-list mail, sorts list traffic by author and function, and draws the
seeded random sample of staff responses that was hand-coded in
hotline-sample-coding.csv.

Codes: P procedural (resend, logistics, transmittal)
       R lookup (answer already exists in a packet page, memo, ordinance,
         regulation or published dataset)
       M mixed (factual scaffold from the record plus staff judgment)
       J judgment (new analysis, policy position, or operational plan)

One coder, n = 40. Treat the shares as a provocation, not a finding.
"""
import json, re, urllib.parse, urllib.request
import pandas as pd

URL = ("https://services.arcgis.com/ePKBjXrBZ2vEEgWd/arcgis/rest/services/"
       "Emails_to_the_City_Council_Hotline/FeatureServer/0/query")
COUNCIL = {"Wallach, Mark", "Benjamin, Matthew", "Schuchard, Ryan",
           "Folkerts, Lauren", "Speer, Nicole", "Marquis, Tina", "Winer, Tara",
           "Brockett, Aaron", "Yates, Bob", "Friend, Rachel", "Adams, Taishya",
           "Joseph, Junie", "Kaplan, Rob"}
SIG = r"(?:Wallach|Benjamin|Schuchard|Folkerts|Speer|Marquis|Winer|Brockett|Yates|Friend|Adams|Joseph|Kaplan|Councilmember|Council Member|Mayor Pro Tem)"

def pull():
    rows, off = [], 0
    while True:
        q = urllib.parse.urlencode({"where": "1=1", "outFields": "*", "f": "json",
                                    "resultOffset": off, "resultRecordCount": 1000,
                                    "orderByFields": "ObjectId"})
        d = json.load(urllib.request.urlopen(URL + "?" + q))
        feats = d.get("features", [])
        rows += [f["attributes"] for f in feats]
        if not d.get("exceededTransferLimit"):
            return pd.DataFrame(rows)
        off += len(feats)

def top_segment(body):
    m = re.search(r"\n?\s*(From:|-----Original Message|On .{5,80} wrote:|________________________________)", body)
    return body[:m.start()] if m and m.start() > 40 else body[:3000]

def categorize(df):
    df = df.copy()
    df["body"] = df.PlainTextBody.fillna("")
    df["subj"] = df.EmailSubject.fillna("")
    lst = df[df.subj.str.contains("BoulderCouncilHotline", case=False)].copy()
    lst["top"] = lst.body.map(top_segment)
    lst["topq"] = lst.top.str.count(r"\?")
    sig = lst.top.str[-600:].str.contains(SIG, regex=True)
    lst["author"] = ["council" if (s in COUNCIL or g) else "staff"
                     for s, g in zip(lst.SentFrom, sig)]
    s = lst.subj.str.lower()
    reply = s.str.contains(r"\bre:|answer|response|follow[- ]?up|information request", regex=True)
    qsub = s.str.contains("question")
    def cat(r, rp, qs):
        if r.author == "council":
            return "council question" if (r.topq >= 1 or qs) else "council position/notice"
        if rp or qs:
            return "staff response"
        if re.search(r"revenue report|disbursement|monthly|quarterly", r.subj.lower()):
            return "staff routine report"
        if re.search(r"agenda|consent|addendum|memo|calendar|cancel|packet|item \d", r.subj.lower()):
            return "staff procedural"
        return "staff other memo"
    lst["cat"] = [cat(r, rp, qs) for r, rp, qs in zip(lst.itertuples(), reply, qsub)]
    return df, lst

if __name__ == "__main__":
    df, lst = categorize(pull())
    print(f"records: {len(df)}  on-list: {len(lst)}  off-list: {len(df) - len(lst)}")
    print(lst.cat.value_counts().to_string())
    q = lst[lst.cat == "council question"]
    print(f"question marks in council question posts: {int(q.topq.sum())}")
    sample = lst[lst.cat == "staff response"].sample(40, random_state=7)
    print("sample ObjectIds:", sorted(sample.ObjectId.tolist()))
