"""Classify every Boulder council hotline message by policy theme and by the
kinds of records a staff member would need to answer or act on it.

Method: transparent keyword dictionaries applied to the subject line plus the
authored top segment of each message (quoted thread text is dropped, so a
reply is not credited with the themes of the message it quotes). Labels are
multi-label: one message can touch several themes and need several kinds of
records. A message that matches no theme is labeled "Meetings and procedure
only"; one that matches no data need is labeled "No records needed".

Dictionaries are deliberately short and legible so a reader can dispute them.
Validation: see the spot-check in the notebook or README that accompanies this
script. Treat results as a map of demand, not as measurement.
"""
import re
import pandas as pd
import hotline_provocation as hp

THEMES = {
    "Budget and finance": r"budget|revenue|sales tax|property tax|\btax(es)?\b|\bbonds?\b|debt|fiscal|appropriat|general fund|financial|disbursement|\bfees?\b|funding|city funds|investment",
    "Housing and land use": r"housing|zoning|land use|density|occupancy|\badus?\b|affordable|development review|annex|bvcp|comprehensive plan|planning reserve|area iii|parking minimum|\bamps\b|site review|cu south|middle housing",
    "Homelessness and human services": r"homeless|unhoused|shelter|safe outdoor|\bsos\b|human services|\bhhs\b|behavioral health|encampment|high utilizer",
    "Public safety and policing": r"police|crime|public safety|oversight panel|\bjttf\b|fire department|firefight|fire-rescue|municipal court|nuisance|enforcement|natural medicine",
    "Wildfire, climate and environment": r"wildfire|climate|emission|\bcwpp\b|water ?wise|resilien|flood|open space|sustainab|energy|xcel|electrif|pollinat|\btrees?\b",
    "Water and utilities": r"\bwater\b|utilit|stormwater|wastewater|\bfiber\b|broadband|\bpower\b",
    "Transportation and airport": r"transport|airport|\bbikes?\b|bicycl|traffic|transit|\broads?\b|mobility|vision zero|trench|parking",
    "Economy and downtown": r"\bdda\b|downtown|economic|business|minimum wage|tipped|\btips?\b|retail|university hill|commercial|library district",
    "Governance, elections and ballot": r"ballot|election|charter|rules of procedure|council rules|code of conduct|mayor pro tem|boards? and commissions?|appoint|policy statement|legislat|polling|campaign|liaison|ethics",
}

DATA_NEEDS = {
    "Financial records": r"budget|revenue|\bcosts?\b|\$\s?\d|funding|\bfunds?\b|\btax|expenditure|debt|appropriat|dollars|financial",
    "Legal and code text": r"ordinance|\bcode\b(?! of conduct)|charter|resolution|rules of procedure|agreement|contract|\bleases?\b|legal|statute|c\.r\.s|state law|regulation",
    "Meeting records": r"\bmemo|packet|\bminutes\b|council direction|previous council|prior council|previously|last year|recording|attachment [a-z]\b|staff report",
    "Plans and studies": r"(master|comprehensive|action|strategic|area|capital|climate|transportation|housing|wildfire|protection|work) ?plans?\b|\bplans? (for|to address)|bvcp|\bstudy\b(?! session)|studies|consultant|assessment|strategy|analysis|\breports?\b",
    "Program and operational data": r"\bdata\b|number of|how many|clients|outcomes?|metrics?|statistic|staffing|\bfte\b|capacity|served|\brates?\b|utilization|performance",
    "Spatial and land records": r"\bmaps?\b|parcel|\bzon(e|es|ing)\b|permits?|annex|acres?|\bsites?\b|neighborhood|subcommunity|corridor|propert(y|ies)(?! tax)",
    "Survey and public input": r"survey|\bpoll|public comment|community input|engagement|feedback|open comment|residents said",
    "External and peer data": r"\bcounty\b|\bthe state\b|state law|state legislat|statewide|state funding|state demograph|federal|drcog|\bcu\b|university|peer|other cities|regional|census|demograph|colorado",
}

BOILERPLATE = [
    r"https?://\S+", r"\[[0-9a-f]{64}\]", r"ATTORNEY-CLIENT PRIVILEGE.*", r"CONFIDENTIALITY NOTICE.*",
    r"1777 Broadway[^\n]*", r"\S*bouldercolorado\.gov\S*", r"City of Boulder,? Colorado",
    r"Boulder,? CO(lorado)?( 80\d{3})?", r"\(?pronouns?[^)\n]*\)?", r"What.s This\??",
    r"Office hours and newsletter[^\n]*", r"subscribe at \S+", r"\S+@\S+",
    r"(Department of )?Housing (and|&) Human Services", r"Planning (and|&) Development Services",
    r"Transportation (and|&) Mobility", r"Facilities (and|&) Fleet", r"Parks (and|&) Recreation",
    r"Open Space (and|&) Mountain Parks", r"City Attorney.?s Office", r"City Manager.?s Office",
    r"Climate Initiatives", r"Community Vitality",
]

def clean(text):
    for pat in BOILERPLATE:
        text = re.sub(pat, " ", text, flags=re.I | re.S)
    return text

def label(text, table):
    t = text.lower()
    return [k for k, pat in table.items() if re.search(pat, t)]

def build(df=None):
    if df is None:
        df = hp.pull()
    _, lst = hp.categorize(df)
    lst = lst.copy()
    lst["text"] = (lst.subj.str.replace(r"\[BoulderCouncilHotline\]", "", regex=True) + " \n " + lst.top.str[:4000]).map(clean)
    lst["date"] = pd.to_datetime(lst.ReceivedDate, utc=True, format="mixed")
    lst["quarter"] = lst.date.dt.tz_convert(None).dt.to_period("Q").astype(str)
    lst["themes"] = lst.text.map(lambda x: label(x, THEMES) or ["Meetings and procedure only"])
    lst["needs"] = lst.text.map(lambda x: label(x, DATA_NEEDS) or ["No records needed"])
    return lst

if __name__ == "__main__":
    lst = build()
    print(lst.explode("themes").themes.value_counts())
    print(lst.explode("needs").needs.value_counts())


QA = {"council question", "staff response"}

def quarterly_theme_share(lst):
    ex = lst.explode("themes")
    n = lst.groupby("quarter").size()
    ct = ex.groupby(["themes", "quarter"]).size().unstack(fill_value=0)
    return (ct / n * 100), n

def qa_need_share(lst):
    qa = lst[lst.cat.isin(QA)]
    return (qa.explode("needs").needs.value_counts() / len(qa) * 100), len(qa)

def theme_by_need(lst):
    qa = lst[lst.cat.isin(QA)].explode("themes").explode("needs").reset_index(drop=True)
    ct = pd.crosstab(qa.themes, qa.needs)
    rows = lst[lst.cat.isin(QA)].explode("themes").themes.value_counts()
    return ct.div(rows, axis=0).mul(100)
