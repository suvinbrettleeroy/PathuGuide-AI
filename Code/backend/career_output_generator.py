"""
Career output generator for Module 2.
Builds a deterministic, structured output object for the career output UI.
"""

from __future__ import annotations

import csv
import os
from datetime import date, timedelta
from typing import Any, Dict, List, Optional
from urllib.parse import quote_plus

DATASET_CANDIDATE_PATHS = [
    r"c:\Users\ASUS\Desktop\Projects\PathGuide AI\Theroy\Career Path Roles.csv",
    os.path.join(os.path.dirname(__file__), "Career Path Roles.csv"),
]

_DATASET_CACHE: List[Dict[str, str]] = []


def _safe_split(value: Optional[str], sep: str = "|") -> List[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(sep) if item and item.strip()]


def _clean_text(value: Optional[str]) -> str:
    if not value:
        return ""
    text = str(value).replace("�", "").strip()
    return " ".join(text.split())


def _split_focus_topics(value: Optional[str]) -> List[str]:
    text = _clean_text(value)
    if not text:
        return []
    for token in [" + ", "+", "|", ";"]:
        text = text.replace(token, ",")
    parts = [p.strip() for p in text.split(",") if p.strip()]
    return parts[:6]


def _dedupe_keep_order(values: List[str]) -> List[str]:
    seen = set()
    result = []
    for value in values:
        key = value.lower().strip()
        if value and key and key not in seen:
            seen.add(key)
            result.append(value)
    return result


def _pick(items: List[str], count: int, fallback: List[str]) -> List[str]:
    selected = [x for x in items if x][:count]
    if len(selected) < count:
        selected.extend(fallback[: count - len(selected)])
    return selected[:count]


def _first_non_empty(values: List[Optional[str]], default: str) -> str:
    for value in values:
        if value and str(value).strip():
            return str(value).strip()
    return default


def _slugify(value: str) -> str:
    cleaned = []
    for ch in (value or "").lower():
        if ch.isalnum():
            cleaned.append(ch)
        else:
            cleaned.append("-")
    slug = "".join(cleaned)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def _load_dataset_rows() -> List[Dict[str, str]]:
    global _DATASET_CACHE
    if _DATASET_CACHE:
        return _DATASET_CACHE

    for path in DATASET_CANDIDATE_PATHS:
        if os.path.exists(path):
            # Some spreadsheet exports are not UTF-8; try safe fallbacks.
            for enc in ["utf-8-sig", "cp1252", "latin-1"]:
                try:
                    with open(path, "r", encoding=enc, newline="") as handle:
                        reader = csv.DictReader(handle)
                        _DATASET_CACHE = [dict(row) for row in reader]
                    break
                except UnicodeDecodeError:
                    continue
            if _DATASET_CACHE:
                break

    return _DATASET_CACHE


def _find_role_row(role: str, domain: str) -> Dict[str, str]:
    rows = _load_dataset_rows()
    role_l = (role or "").strip().lower()
    domain_l = (domain or "").strip().lower()

    best_match: Dict[str, str] = {}
    for row in rows:
        row_role = (row.get("Role_Name") or "").strip().lower()
        row_domain = (row.get("Domain") or "").strip().lower()
        if row_role == role_l and row_domain == domain_l:
            return row
        if row_role == role_l and not best_match:
            best_match = row

    return best_match


def _normalize_study_hours(value: str) -> str:
    mapping = {
        "1-2 hours": "1-2 hours",
        "2-4 hours": "2-4 hours",
        "4-6 hours": "4-6 hours",
        "6-8 hours": "6-8 hours",
        "8+ hours": "More than 8 hours",
        "more than 8 hours": "More than 8 hours",
    }
    return mapping.get((value or "").strip(), (value or "2-4 hours").strip() or "2-4 hours")


def _study_hours_score(study_hours: str) -> int:
    normalized = _normalize_study_hours(study_hours)
    return {
        "1-2 hours": 8,
        "2-4 hours": 14,
        "4-6 hours": 20,
        "6-8 hours": 23,
        "More than 8 hours": 25,
    }.get(normalized, 14)


def _timeline_score(months: int) -> int:
    return {3: 14, 6: 22, 12: 25}.get(months, 22)


def _trend_from_row(row: Dict[str, str]) -> str:
    demand = (row.get("Hiring_Demand_Level") or "").strip().lower()
    if demand in ["very high", "high"]:
        return "Growing"
    if demand in ["medium", "moderate"]:
        return "Stable"
    if demand in ["low"]:
        return "Competitive"
    return "Stable"


def _market_score(trend: str) -> int:
    return {
        "Growing": 22,
        "Emerging": 20,
        "Stable": 18,
        "Competitive": 16,
        "Niche": 14,
    }.get(trend, 18)


def _education_score(department: str, domain: str) -> int:
    dep = (department or "").lower()
    dom = (domain or "").lower()

    strong_pairs = [
        (("computer", "it", "data", "ai"), ("software", "data", "ai", "cloud", "web", "cyber")),
        (("electronics", "ece"), ("embedded", "vlsi", "iot", "signal", "automation")),
        (("mechanical",), ("mechanical", "automobile", "cad", "production", "robotics")),
        (("civil",), ("civil", "construction", "structural", "water", "geotechnical")),
        (("electrical", "eee"), ("power", "electrical", "automation", "renewable", "control")),
    ]

    for dep_keys, dom_keys in strong_pairs:
        if any(k in dep for k in dep_keys) and any(k in dom for k in dom_keys):
            return 22

    if any(token in dep for token in ["computer", "it", "engineering", "science"]) and any(
        token in dom for token in ["development", "analytics", "technology", "engineering"]
    ):
        return 16

    if dep and dom:
        return 10
    return 14


def _rating_label(score: int) -> str:
    if score >= 80:
        return "High"
    if score >= 60:
        return "Medium"
    return "Low"


def _stars(score: int) -> int:
    if score <= 39:
        return 2
    if score <= 59:
        return 3
    if score <= 79:
        return 4
    return 5


def _roadmap_mode(months: int) -> str:
    return {3: "Quick Start Mode", 6: "Balanced Mode", 12: "Comprehensive Mode"}.get(months, "Balanced Mode")


def _roadmap_phases(
    months: int,
    monthly_focus: List[str],
    beginner_projects: List[str],
    intermediate_projects: List[str],
    advanced_projects: List[str],
) -> List[Dict[str, Any]]:
    defaults = [
        "Foundations and role basics",
        "Core tools and workflows",
        "Applied practice and projects",
        "Advanced concepts",
        "Portfolio polishing",
        "Interview preparation",
        "Domain specialization",
        "Case studies",
        "Optimization techniques",
        "Capstone planning",
        "Capstone execution",
        "Job applications and mocks",
    ]
    focus = monthly_focus + defaults

    def phase(title: str, months_label: str, weeks: str, idx: List[int]) -> Dict[str, Any]:
        topics: List[str] = []
        for i in idx:
            if i < len(focus):
                topics.extend(_split_focus_topics(focus[i]))
        topics = _dedupe_keep_order(topics)

        deliverables_seed = [
            "Complete one focused mini project",
            "Publish progress notes in portfolio",
            "Solve practice exercises with review",
            "Share outcomes with mentor/peer",
        ]
        if any(i <= 2 for i in idx):
            deliverables_seed.extend(beginner_projects[:1])
        elif any(3 <= i <= 6 for i in idx):
            deliverables_seed.extend(intermediate_projects[:1])
        else:
            deliverables_seed.extend(advanced_projects[:1])

        return {
            "phase_title": title,
            "months": months_label,
            "weeks_range": weeks,
            "bullet_topics": _pick(
                topics,
                5,
                [
                    "Concept revision and note making",
                    "Hands-on practice with core tools",
                    "Weekly quiz and recap",
                    "Case-based problem solving",
                    "Communication of outcomes",
                ],
            ),
            "practice_deliverables": _pick(
                deliverables_seed,
                3,
                ["Submit one project", "Document learnings", "Do one mock session"],
            ),
        }

    if months == 3:
        return [
            phase("Month 1", "Month 1", "Weeks 1-4", [0, 1, 2]),
            phase("Month 2", "Month 2", "Weeks 5-8", [3, 4, 5]),
            phase("Month 3", "Month 3", "Weeks 9-12", [6, 7, 8]),
        ]
    if months == 12:
        return [
            phase("Quarter 1", "Months 1-3", "Weeks 1-12", [0, 1, 2]),
            phase("Quarter 2", "Months 4-6", "Weeks 13-24", [3, 4, 5]),
            phase("Quarter 3", "Months 7-9", "Weeks 25-36", [6, 7, 8]),
            phase("Quarter 4", "Months 10-12", "Weeks 37-48", [9, 10, 11]),
        ]

    return [
        phase("Phase 1", "Months 1-2", "Weeks 1-8", [0, 1]),
        phase("Phase 2", "Months 3-4", "Weeks 9-16", [2, 3]),
        phase("Phase 3", "Months 5-6", "Weeks 17-24", [4, 5]),
    ]


def _time_split(study_hours: str) -> Dict[str, str]:
    normalized = _normalize_study_hours(study_hours)
    if normalized == "1-2 hours":
        return {"theory": "30 min", "practice": "40 min", "revision": "10 min", "mock_or_projects": "10 min"}
    if normalized == "2-4 hours":
        return {"theory": "50 min", "practice": "80 min", "revision": "30 min", "mock_or_projects": "20 min"}
    if normalized == "4-6 hours":
        return {"theory": "90 min", "practice": "120 min", "revision": "40 min", "mock_or_projects": "40 min"}
    if normalized == "6-8 hours":
        return {"theory": "120 min", "practice": "180 min", "revision": "60 min", "mock_or_projects": "60 min"}
    return {"theory": "150 min", "practice": "210 min", "revision": "70 min", "mock_or_projects": "70 min"}


def _format_lpa(min_inr: str, max_inr: str, fallback: str) -> str:
    try:
        min_val = int(float(min_inr))
        max_val = int(float(max_inr))
        return f"{min_val / 100000:.1f}-{max_val / 100000:.1f} LPA"
    except Exception:
        return fallback


def _format_currency(min_val: str, max_val: str, currency: str, fallback: str) -> str:
    try:
        lo = int(float(min_val))
        hi = int(float(max_val))
        return f"{currency} {lo:,}-{hi:,}"
    except Exception:
        return fallback


def _translate(lang: str, en: str, ta: str) -> str:
    return ta if lang == "ta" else en


def _resource_url(resource_name: str, role: str, domain: str, kind: str) -> str:
    name = (resource_name or "").strip()
    name_l = name.lower()

    if name.startswith("http://") or name.startswith("https://"):
        return name

    if kind == "free":
        if "microsoft learn" in name_l or "azure" in name_l:
            return "https://learn.microsoft.com/training/"
        if "aws skill builder" in name_l:
            return "https://explore.skillbuilder.aws/learn"
        if "nptel" in name_l:
            return "https://nptel.ac.in/courses"
        if "swayam" in name_l:
            return "https://swayam.gov.in/"
        if "github" in name_l:
            return "https://skills.github.com/"
        if "leetcode" in name_l:
            return "https://leetcode.com/studyplan/"
        if "hackerrank" in name_l:
            return "https://www.hackerrank.com/skills-verification"
        if "roadmap" in name_l:
            return "https://roadmap.sh/"
        if "mode" in name_l and "sql" in name_l:
            return "https://mode.com/sql-tutorial/"
        if "kaggle" in name_l:
            return "https://www.kaggle.com/learn"
        if "khan" in name_l or "statistics" in name_l:
            return "https://www.khanacademy.org/math/statistics-probability"
        if "tableau" in name_l:
            return "https://www.tableau.com/learn/training"
        if "python" in name_l:
            return "https://docs.python.org/3/tutorial/"
        if "sql" in name_l:
            return "https://www.w3schools.com/sql/"
        if "freecodecamp" in name_l:
            return "https://www.freecodecamp.org/learn"
        if "geeksforgeeks" in name_l:
            return "https://www.geeksforgeeks.org/courses/"
        if "kdnuggets" in name_l:
            return "https://www.kdnuggets.com/"
        if "analytics vidhya" in name_l:
            return "https://www.analyticsvidhya.com/learn/"
        if "mdn" in name_l:
            return "https://developer.mozilla.org/en-US/docs/Learn"
        if "official documentation" in name_l:
            return "https://roadmap.sh/"
        if "community tutorials" in name_l:
            return "https://www.freecodecamp.org/learn"
        if "practice portal" in name_l:
            return "https://leetcode.com/studyplan/"
        return "https://roadmap.sh/"
    if kind == "paid":
        if "udemy" in name_l:
            return "https://www.udemy.com/courses/development/"
        if "coursera" in name_l:
            return "https://www.coursera.org/courses"
        if "edx" in name_l:
            return "https://www.edx.org/learn"
        if "simplilearn" in name_l:
            return "https://www.simplilearn.com/skillup-free-online-courses"
        if "guvi" in name_l:
            return "https://www.guvi.in/courses/"
        if "scaler" in name_l:
            return "https://www.scaler.com/courses/"
        if "upgrad" in name_l:
            return "https://www.upgrad.com/courses/"
        if "great learning" in name_l:
            return "https://www.mygreatlearning.com/academy"
        if "intellipaat" in name_l:
            return "https://intellipaat.com/courses/"
        if "mentor-led" in name_l or "structured bootcamp" in name_l or "career track" in name_l:
            return "https://www.coursera.org/career-academy"
        return "https://www.coursera.org/courses"
    if kind == "cert":
        if "google data analytics" in name_l:
            return "https://www.coursera.org/professional-certificates/google-data-analytics"
        if "pl-300" in name_l or "power bi" in name_l:
            return "https://learn.microsoft.com/en-us/credentials/certifications/power-bi-data-analyst-associate/"
        if "tableau" in name_l and "specialist" in name_l:
            return "https://www.tableau.com/learn/certification/desktop-specialist"
        if "ibm data science" in name_l or "ibm" in name_l:
            return "https://www.coursera.org/professional-certificates/ibm-data-science"
        if "tensorflow" in name_l:
            return "https://www.tensorflow.org/certificate"
        if "aws" in name_l:
            return "https://aws.amazon.com/certification/"
        if "oracle" in name_l or "java" in name_l:
            return "https://education.oracle.com/certification"
        if "azure" in name_l or "microsoft" in name_l:
            return "https://learn.microsoft.com/en-us/credentials/certifications/"
        if "mongodb" in name_l:
            return "https://learn.mongodb.com/"
        if "pmp" in name_l:
            return "https://www.pmi.org/certifications/project-management-pmp"
        if "scrum" in name_l:
            return "https://www.scrum.org/professional-scrum-certifications"
        if "role-aligned certification" in name_l or "tool specialization certificate" in name_l:
            return "https://www.coursera.org/professional-certificates"
        return "https://www.coursera.org/professional-certificates"
    if kind == "apply":
        if "government" in domain.lower():
            return "https://www.tnpsc.gov.in/"
        if "data" in domain.lower() or "ai" in domain.lower() or "ml" in domain.lower():
            return "https://www.linkedin.com/jobs/data-analyst-jobs/"
        if "cloud" in domain.lower() or "devops" in domain.lower():
            return "https://www.linkedin.com/jobs/cloud-engineer-jobs/"
        if "software" in domain.lower() or "web" in domain.lower():
            return "https://www.linkedin.com/jobs/software-engineer-jobs/"
        return f"https://www.linkedin.com/jobs/search/?keywords={quote_plus(role + ' ' + domain)}"
    return "https://www.coursera.org/"


def _tool_category(name: str) -> str:
    n = (name or "").lower()
    if any(k in n for k in ["python", "java", "javascript", "typescript", "c++", "r ", "r-lang"]):
        return "Programming"
    if any(k in n for k in ["sql", "mysql", "postgres", "oracle", "mongodb", "database"]):
        return "Database"
    if any(k in n for k in ["power bi", "tableau", "excel", "looker"]):
        return "Analytics/BI"
    if any(k in n for k in ["aws", "azure", "gcp", "cloud", "docker", "kubernetes", "devops"]):
        return "Cloud/DevOps"
    if any(k in n for k in ["git", "github", "jira", "agile"]):
        return "Workflow"
    if any(k in n for k in ["tensorflow", "pytorch", "scikit", "ml", "ai"]):
        return "AI/ML"
    return "Core"


def _build_tools_for_role(role: str, domain: str, skills: List[str]) -> List[Dict[str, str]]:
    seed = list(skills)
    role_l = role.lower()
    domain_l = domain.lower()

    if any(k in role_l or k in domain_l for k in ["data", "analyst", "analytics"]):
        seed.extend(["SQL", "Python", "Power BI", "Tableau", "Excel"])
    if any(k in role_l or k in domain_l for k in ["software", "developer", "web", "full stack"]):
        seed.extend(["Git", "JavaScript", "Node.js", "React", "SQL"])
    if any(k in role_l or k in domain_l for k in ["cloud", "devops", "sre"]):
        seed.extend(["AWS", "Azure", "Docker", "Kubernetes", "Terraform"])
    if any(k in role_l or k in domain_l for k in ["ai", "ml", "machine learning"]):
        seed.extend(["Python", "TensorFlow", "PyTorch", "SQL", "MLOps"])

    uniq = _pick(_dedupe_keep_order([x for x in seed if x]), 6, ["Python", "SQL", "Git", "Excel", "Cloud", "Communication"])
    return [
        {
            "name": name,
            "category": _tool_category(name),
            "why": f"Useful for {role} workflows in {domain}.",
        }
        for name in uniq
    ]


def _build_domain_role_catalog(rows: List[Dict[str, str]], selected_domain: str, selected_role: str) -> List[Dict[str, Any]]:
    bucket: Dict[str, List[Dict[str, str]]] = {}
    for row in rows:
        dom = _clean_text(row.get("Domain", ""))
        role = _clean_text(row.get("Role_Name", ""))
        if not dom or not role:
            continue
        bucket.setdefault(dom, [])
        bucket[dom].append(row)

    result: List[Dict[str, Any]] = []
    for dom, domain_rows in bucket.items():
        roles = _dedupe_keep_order([_clean_text(r.get("Role_Name", "")) for r in domain_rows])
        role_cards: List[Dict[str, str]] = []
        for r in domain_rows[:8]:
            role_name = _clean_text(r.get("Role_Name", ""))
            if not role_name:
                continue
            role_cards.append(
                {
                    "role": role_name,
                    "demand": _clean_text(r.get("Hiring_Demand_Level", "")) or "Medium",
                    "fresher_salary": _clean_text(r.get("Avg_Package_Fresher_LPA", "")) or "4-6 LPA",
                    "key_skill": _first_non_empty([
                        _clean_text(r.get("Core_Skill_1", "")),
                        _clean_text(r.get("Important_Skill_1", "")),
                    ], "Problem Solving"),
                    "key_tool": _first_non_empty([
                        _clean_text(r.get("Core_Skill_2", "")),
                        _clean_text(r.get("Core_Skill_3", "")),
                    ], "Industry toolset"),
                    "starter_project": _first_non_empty([
                        _clean_text(r.get("Project_1", "")),
                        _clean_text(r.get("Project_2", "")),
                    ], f"Starter {role_name} Project"),
                }
            )

        result.append(
            {
                "domain": dom,
                "roles": roles[:20],
                "selected": dom == selected_domain,
                "apply_link": _resource_url(dom, selected_role, dom, "apply"),
                "role_cards": role_cards,
            }
        )

    result.sort(key=lambda x: (0 if x["selected"] else 1, x["domain"].lower()))
    return result


def _project_features(title: str, role: str) -> List[str]:
    title_l = title.lower()
    features: List[str] = []
    if "dashboard" in title_l:
        features.extend([
            "Interactive KPI cards and filters",
            "Trend and comparison charts",
            "Export-ready reporting layout",
        ])
    if "analysis" in title_l or "analytics" in title_l:
        features.extend([
            "Data cleaning and transformation workflow",
            "Insight generation with clear metrics",
            "Business recommendation summary",
        ])
    if "forecast" in title_l or "prediction" in title_l:
        features.extend([
            "Model baseline and evaluation",
            "Error tracking and improvement cycle",
            "Result interpretation for stakeholders",
        ])
    if "sql" in title_l:
        features.extend([
            "Complex joins and aggregations",
            "Reusable query structure",
            "Performance-aware query design",
        ])
    if not features:
        features = [
            f"End-to-end {role} workflow",
            "Clear documentation and reproducible steps",
            "Portfolio-ready output with visuals",
        ]
    return _pick(_dedupe_keep_order(features), 3, features)


def _application_links(role: str, domain: str) -> List[Dict[str, str]]:
    query = quote_plus(f"{role} {domain}".strip())
    if "government" in (domain or "").lower():
        return [
            {"name": "TNPSC", "url": "https://www.tnpsc.gov.in/"},
            {"name": "UPSC", "url": "https://upsc.gov.in/"},
            {"name": "SSC", "url": "https://ssc.nic.in/"},
            {"name": "Employment News", "url": "https://www.employmentnews.gov.in/"},
        ]
    return [
        {"name": "LinkedIn Jobs", "url": f"https://www.linkedin.com/jobs/search/?keywords={query}"},
        {"name": "Naukri", "url": f"https://www.naukri.com/jobs-in-india?keyword={query}"},
        {"name": "Indeed", "url": f"https://in.indeed.com/jobs?q={query}"},
        {"name": "Foundit", "url": f"https://www.foundit.in/srp/results?query={query}"},
    ]


def build_career_output(user_data: Dict[str, Any], selection: Dict[str, str], language: str) -> Dict[str, Any]:
    role = selection.get("role") or user_data.get("role") or "Data Analyst"
    domain = selection.get("domain") or user_data.get("domain") or "Data Science & Analytics"
    row = _find_role_row(role, domain)

    study_hours_option = _normalize_study_hours(user_data.get("study_hours", "2-4 hours"))
    try:
        roadmap_months = int(user_data.get("roadmap_months") or user_data.get("roadmap_duration") or 6)
    except Exception:
        roadmap_months = 6
    if roadmap_months not in [3, 6, 12]:
        roadmap_months = 6

    current_date = user_data.get("current_date") or date.today().isoformat()
    try:
        today = date.fromisoformat(current_date)
    except Exception:
        today = date.today()
        current_date = today.isoformat()

    trend = _trend_from_row(row)

    edu = _education_score(user_data.get("department", ""), domain)
    learn = _study_hours_score(study_hours_option)
    time = _timeline_score(roadmap_months)
    market = _market_score(trend)
    overall = min(100, edu + learn + time + market)

    rows = _load_dataset_rows()

    daily_responsibilities = _pick(
        _safe_split(_clean_text(row.get("Daily_Responsibilities", ""))),
        6,
        [
            "Analyze assigned tasks and clarify requirements",
            "Prepare clean and structured working data",
            "Build and validate outputs using core tools",
            "Share insights with team and stakeholders",
            "Document assumptions and results",
            "Review progress and plan next actions",
        ],
    )

    core_skills = _dedupe_keep_order([
        _clean_text(row.get("Core_Skill_1", "")),
        _clean_text(row.get("Core_Skill_2", "")),
        _clean_text(row.get("Core_Skill_3", "")),
        _clean_text(row.get("Core_Skill_4", "")),
        _clean_text(row.get("Important_Skill_1", "")),
        _clean_text(row.get("Important_Skill_2", "")),
    ])
    support_skills = _dedupe_keep_order([
        _clean_text(row.get("Important_Skill_3", "")),
        _clean_text(row.get("Good_To_Have_Skill_1", "")),
        _clean_text(row.get("Good_To_Have_Skill_2", "")),
        _clean_text(row.get("Soft_Skill_1", "")),
        _clean_text(row.get("Soft_Skill_2", "")),
        _clean_text(row.get("Soft_Skill_3", "")),
        _clean_text(row.get("Soft_Skill_4", "")),
        _clean_text(row.get("Soft_Skill_5", "")),
    ])
    tools = _dedupe_keep_order([
        _clean_text(row.get("Core_Skill_1", "")),
        _clean_text(row.get("Core_Skill_2", "")),
        _clean_text(row.get("Core_Skill_3", "")),
        _clean_text(row.get("Core_Skill_4", "")),
        _clean_text(row.get("Important_Skill_1", "")),
    ])

    free_resources = _dedupe_keep_order([
        _clean_text(row.get("Free_Resource_1", "")),
        _clean_text(row.get("Free_Resource_2", "")),
        _clean_text(row.get("Free_Resource_3", "")),
        _clean_text(row.get("Free_Resource_4", "")),
    ])
    paid_resources = _dedupe_keep_order([
        _clean_text(row.get("Paid_Course_1", "")),
        _clean_text(row.get("Paid_Course_2", "")),
        _clean_text(row.get("Paid_Course_3", "")),
    ])
    certs = _dedupe_keep_order([
        _clean_text(row.get("Certification_1", "")),
        _clean_text(row.get("Certification_2", "")),
    ])

    beginner_projects = _pick(
        _dedupe_keep_order([_clean_text(row.get("Project_1", "")), _clean_text(row.get("Project_2", ""))]),
        2,
        ["Beginner project 1", "Beginner project 2"],
    )
    intermediate_projects = _pick(
        _dedupe_keep_order([_clean_text(row.get("Project_3", "")), _clean_text(row.get("Project_4", ""))]),
        2,
        ["Intermediate project 1", "Intermediate project 2"],
    )
    advanced_projects = _pick(
        _dedupe_keep_order([
            _clean_text(row.get("Project_5", "")),
            _clean_text(row.get("Project_6", "")),
            _clean_text(row.get("Project_7", "")),
        ]),
        2,
        ["Advanced project 1", "Advanced project 2"],
    )

    monthly_focus = [_clean_text(row.get(f"Month_{i}_Focus", "")) for i in range(1, 13)]
    phases = _roadmap_phases(
        roadmap_months,
        [x for x in monthly_focus if x],
        beginner_projects,
        intermediate_projects,
        advanced_projects,
    )
    focus_topic = phases[0]["bullet_topics"][0] if phases else "Core concept practice"

    all_companies = _dedupe_keep_order([
        _clean_text(row.get("Top_Company_1", "")),
        _clean_text(row.get("Top_Company_2", "")),
        _clean_text(row.get("Top_Company_3", "")),
        _clean_text(row.get("Top_Company_4", "")),
        _clean_text(row.get("Top_Company_5", "")),
        _clean_text(row.get("Top_Company_6", "")),
        _clean_text(row.get("Top_Company_7", "")),
        _clean_text(row.get("Top_Company_8", "")),
        _clean_text(row.get("Top_Company_9", "")),
        _clean_text(row.get("Top_Company_10", "")),
    ])

    quick_summary = _translate(
        language,
        f"{role} is a practical career path with {trend.lower()} demand when you follow your {roadmap_months}-month plan consistently.",
        f"{role} ஒரு நல்ல தொழில் பாதை. உங்கள் {roadmap_months} மாத திட்டத்தை தொடர்ந்து பின்பற்றினால் நல்ல வாய்ப்புகள் கிடைக்கும்.",
    )

    rating_label = _rating_label(overall)

    data = {
        "header": {
            "title": _translate(language, "Your Career Roadmap", "உங்கள் தொழில் பாதை திட்டம்"),
            "subtitle": f"{user_data.get('name', '').strip() or 'Student'} - {user_data.get('degree', 'Degree')} - {user_data.get('department', 'Department')}",
            "role": role,
            "domain": domain,
            "roadmap_duration_months": roadmap_months,
            "study_hours_option": study_hours_option,
            "quick_summary_line": quick_summary,
        },
        "success_prediction": {
            "overall_success_score": overall,
            "star_rating": _stars(overall),
            "rating_label": rating_label,
            "factor_breakdown": {
                "education_fit": {
                    "score": edu,
                    "max": 25,
                    "explanation": _translate(language, "Your department and selected domain alignment.", "உங்கள் துறை மற்றும் தேர்ந்தெடுத்த களத்தின் பொருத்தம்."),
                },
                "learning_commitment": {
                    "score": learn,
                    "max": 25,
                    "explanation": _translate(language, f"Based on {study_hours_option} daily study commitment.", f"தினசரி {study_hours_option} படிப்பு நேரத்தை அடிப்படையாக கொண்டு."),
                },
                "timeline_realism": {
                    "score": time,
                    "max": 25,
                    "explanation": _translate(language, f"{roadmap_months}-month timeline feasibility.", f"{roadmap_months} மாத கால அட்டவணை நடைமுறைபடுத்தும் சாத்தியம்."),
                },
                "market_demand": {
                    "score": market,
                    "max": 25,
                    "explanation": _translate(language, f"Current market trend is {trend}.", f"தற்போதைய சந்தை போக்கு: {trend}."),
                },
            },
            "how_to_improve": _pick(
                [
                    row.get("Success_Tips_1", ""),
                    row.get("Success_Tips_2", ""),
                    row.get("Success_Tips_3", ""),
                    row.get("Success_Tips_4", ""),
                    row.get("Success_Tips_5", ""),
                ],
                5,
                [
                    "Stay consistent with daily study schedule",
                    "Build portfolio projects and publish code",
                    "Practice interview questions weekly",
                    "Improve communication and documentation",
                    "Apply regularly and track feedback",
                ],
            ),
        },
        "role_overview": {
            "what_is_this_role": _first_non_empty(
                [
                    row.get("Role_Description"),
                    _translate(language, "This role focuses on solving business and technical problems using structured methods and tools.", "இந்த பணி திட்டமிட்ட முறையில் கருவிகள் மூலம் வணிக மற்றும் தொழில்நுட்ப சிக்கல்களை தீர்க்கிறது."),
                ],
                "Role overview",
            ),
            "daily_responsibilities": daily_responsibilities,
            "quick_stats": {
                "experience_to_start": row.get("Experience_Required", "0-2 years (typical)"),
                "work_type": row.get("Work_Type", "Varies"),
                "industry": row.get("Industry", "Multiple industries"),
                "job_openings_annual_india": _clean_text(row.get("Job_Openings_Annual_India", "")) or "High demand in many industries",
                "avg_package_fresher_lpa": _clean_text(row.get("Avg_Package_Fresher_LPA", "")) or "4-6 LPA",
            },
            "why_this_career": [
                {
                    "title": _translate(language, "Good Demand", "நல்ல தேவை"),
                    "description": _first_non_empty([row.get("Why_This_Career_1")], _translate(language, "High demand in many industries", "பல துறைகளில் நல்ல தேவை உள்ளது")),
                },
                {
                    "title": _translate(language, "Career Growth", "தொழில் வளர்ச்சி"),
                    "description": _first_non_empty([row.get("Why_This_Career_2")], _translate(language, "Clear growth path with experience", "அனுபவத்துடன் தெளிவான வளர்ச்சி பாதை")),
                },
                {
                    "title": _translate(language, "Good Salary", "நல்ல சம்பளம்"),
                    "description": _first_non_empty([row.get("Why_This_Career_3")], _translate(language, "Competitive salary progression", "போட்டித்திறன் கொண்ட சம்பள வளர்ச்சி")),
                },
                {
                    "title": _translate(language, "Work-Life Balance", "வேலை-வாழ்க்கை சமநிலை"),
                    "description": _first_non_empty([row.get("Why_This_Career_4")], _translate(language, "Balanced work options are available", "சமநிலை வாய்ப்புகள் கிடைக்கின்றன")),
                },
            ],
        },
        "personalized_roadmap": {
            "mode_label": _roadmap_mode(roadmap_months),
            "phases": phases,
        },
        "study_plan": {
            "weekly_checklist": _pick(
                [
                    _translate(language, "Finish planned theory topics", "திட்டமிட்ட கோட்பாட்டு தலைப்புகளை முடிக்கவும்"),
                    _translate(language, "Complete hands-on practice tasks", "நடைமுறை பயிற்சி பணிகளை முடிக்கவும்"),
                    _translate(language, "Revise key notes and formulas", "முக்கிய குறிப்புகள் மற்றும் சூத்திரங்களை மீளாய்வு செய்யவும்"),
                    _translate(language, "Take one timed mock or coding test", "ஒரு நேரமிட்ட மாதிரி தேர்வு/கோடிங் சோதனை எழுதவும்"),
                    _translate(language, "Update portfolio or learning log", "Portfolio அல்லது கற்றல் பதிவை புதுப்பிக்கவும்"),
                    _translate(language, "Review weak areas and fix gaps", "பலவீன பகுதிகளை சரிசெய்யவும்"),
                    _translate(language, "Plan next week's goals", "அடுத்த வார இலக்குகளை திட்டமிடவும்"),
                ],
                7,
                ["Daily study", "Practice", "Revise", "Mock", "Portfolio", "Review", "Plan"],
            ),
            "time_split_per_day": _time_split(study_hours_option),
            "today_task": {
                "date": current_date,
                "focus_topic": focus_topic,
                "learning_goal": _translate(language, "Build practical confidence in today's focus topic.", "இன்றைய தலைப்பில் நடைமுறை நம்பிக்கை பெறுதல்."),
                "morning_plan": _pick(
                    [
                        _translate(language, "Review previous notes for 20 minutes", "முந்தைய குறிப்புகளை 20 நிமிடங்கள் மீளாய்வு செய்யவும்"),
                        _translate(language, "Study one core concept deeply", "ஒரு முக்கிய கருத்தை ஆழமாக படிக்கவும்"),
                        _translate(language, "Take short self-quiz", "சிறிய சுய வினாடி வினா செய்யவும்"),
                    ],
                    3,
                    ["Review", "Study", "Quiz"],
                ),
                "evening_plan": _pick(
                    [
                        _translate(language, "Do practical exercises", "நடைமுறை பயிற்சிகள் செய்யவும்"),
                        _translate(language, "Document what you learned", "கற்றவற்றை பதிவு செய்யவும்"),
                        _translate(language, "Prepare tomorrow task list", "நாளைய பணிப் பட்டியல் தயாரிக்கவும்"),
                    ],
                    3,
                    ["Practice", "Document", "Plan"],
                ),
                "checklist": _pick(
                    [
                        "Complete one focused lesson",
                        "Solve one practical assignment",
                        "Revise key points",
                        "Track doubts/questions",
                        "Update progress notes",
                        "Prepare next-day plan",
                    ],
                    6,
                    ["Lesson", "Practice", "Revision", "Doubts", "Notes", "Next day"],
                ),
                "yesterday_review": _translate(language, "Continue from yesterday's unfinished tasks and summarize learnings.", "நேற்றைய நிறைவடையாத பணிகளை தொடரவும் மற்றும் கற்றதை சுருக்கவும்."),
                "tomorrow_preview": _translate(language, "Move to the next sub-topic and increase practical complexity slightly.", "அடுத்த துணைத்தலைப்புக்கு சென்று நடைமுறை சிக்கல்தன்மையை சிறிது உயர்த்தவும்."),
                "progress": {"weekly_percent": 35, "overall_percent": 18, "streak_days": 4},
            },
        },
        "skills_and_tools": {
            "core_skills": [
                {"name": name, "priority": "Must-have", "why": _translate(language, "Core requirement for this role.", "இந்த பணிக்கான அடிப்படைத் திறன்.")}
                for name in _pick([x for x in core_skills if x], 5, ["Problem solving", "Core tools", "Data handling", "Communication", "Practice discipline"])
            ],
            "supporting_skills": [
                {"name": name, "priority": "Good-to-have", "why": _translate(language, "Improves productivity and collaboration.", "உற்பத்தித்திறன் மற்றும் ஒத்துழைப்பை மேம்படுத்தும்.")}
                for name in _pick([x for x in support_skills if x], 5, ["Version control", "Documentation", "Presentation", "Teamwork", "Adaptability"])
            ],
            "tools_technologies": _build_tools_for_role(role, domain, [x for x in tools if x]),
            "role_fit_summary": _translate(
                language,
                f"These skills and tools are prioritized for {role} in {domain}, based on current role expectations.",
                f"இந்த திறன்கள் மற்றும் கருவிகள் {domain} துறையில் {role} பணிக்கான தற்போதைய எதிர்பார்ப்புகளின் அடிப்படையில் தேர்ந்தெடுக்கப்பட்டவை.",
            ),
            "learning_sequence": [
                _translate(language, "Start with role fundamentals and vocabulary", "பணியின் அடிப்படை கருத்துக்கள் மற்றும் சொற்களுடன் தொடங்கவும்"),
                _translate(language, "Practice core tools on small tasks", "முக்கிய கருவிகளை சிறிய பணிகளில் பயிற்சி செய்யவும்"),
                _translate(language, "Build one mini project and document it", "ஒரு சிறிய திட்டத்தை உருவாக்கி ஆவணப்படுத்தவும்"),
                _translate(language, "Move to role-level case studies", "பணி நிலை case study-களுக்கு நகரவும்"),
                _translate(language, "Prepare interviews with portfolio evidence", "portfolio ஆதாரத்துடன் நேர்முகத்தேர்வுக்கு தயாராகவும்"),
            ],
        },
        "courses_and_resources": {
            "free_resources": [
                {
                    "name": name,
                    "platform": "Official learning source",
                    "duration": "Self-paced",
                    "cost": "Free",
                    "url": _resource_url(name, role, domain, "free"),
                }
                for name in _pick([x for x in free_resources if x], 3, ["Official documentation", "Community tutorials", "Practice portal"])
            ],
            "paid_or_mixed_resources": [
                {
                    "name": name,
                    "platform": "Learning platform",
                    "duration": "4-12 weeks",
                    "cost": "Paid",
                    "url": _resource_url(name, role, domain, "paid"),
                }
                for name in _pick([x for x in paid_resources if x], 3, ["Structured bootcamp", "Career track course", "Mentor-led workshop"])
            ],
            "recommended_certifications": [
                {
                    "name": name,
                    "provider": "Industry provider",
                    "duration": "2-6 months",
                    "cost": "Varies",
                    "why": _translate(language, "Helps validate practical capability.", "நடைமுறை திறனை உறுதி செய்ய உதவும்."),
                    "url": _resource_url(name, role, domain, "cert"),
                }
                for name in _pick([x for x in certs if x], 2, ["Role-aligned certification", "Tool specialization certificate"])
            ],
            "budget_note": _translate(
                language,
                f"Budget selected: {user_data.get('budget', 'Skip')}. Start with free resources and add paid options when needed.",
                f"தேர்ந்தெடுத்த பட்ஜெட்: {user_data.get('budget', 'Skip')}. முதலில் இலவச வளங்களால் தொடங்கி தேவைக்கு ஏற்ப கட்டண பாடங்களை சேர்க்கவும்.",
            ),
            "application_links": _application_links(role, domain),
        },
        "projects": {
            "beginner": [
                {
                    "title": title,
                    "description": _translate(language, "Beginner-level project to apply fundamentals.", "அடிப்படைத் திறன்களைப் பயன்படுத்தும் தொடக்க நிலை திட்டம்."),
                    "skills_used": _pick([x for x in core_skills if x], 3, ["Fundamentals", "Practice", "Documentation"]),
                    "duration": "1-2 weeks",
                    "outcome": _translate(language, "Portfolio-ready mini deliverable.", "Portfolio-க்கு பொருத்தமான சிறிய வெளியீடு."),
                    "features": _project_features(title, role),
                }
                for title in beginner_projects
            ],
            "intermediate": [
                {
                    "title": title,
                    "description": _translate(language, "Intermediate project with integrated workflow.", "இடைநிலை ஒருங்கிணைந்த பணிச்சுற்று திட்டம்."),
                    "skills_used": _pick([x for x in core_skills if x], 4, ["Core tools", "Analysis", "Testing", "Communication"]),
                    "duration": "2-4 weeks",
                    "outcome": _translate(language, "Demonstrates practical problem-solving ability.", "நடைமுறை சிக்கல் தீர்க்கும் திறனை காட்டும்."),
                    "features": _project_features(title, role),
                }
                for title in intermediate_projects
            ],
            "advanced": [
                {
                    "title": title,
                    "description": _translate(language, "Advanced capstone-style implementation.", "மேம்பட்ட capstone வகை செயலாக்கம்."),
                    "skills_used": _pick([x for x in core_skills if x], 5, ["Architecture", "Optimization", "Delivery", "Documentation", "Review"]),
                    "duration": "4-8 weeks",
                    "outcome": _translate(language, "Strong portfolio evidence for interviews.", "நேர்முகத்திற்கான வலுவான portfolio ஆதாரம்."),
                    "features": _project_features(title, role),
                }
                for title in advanced_projects
            ],
            "portfolio_tips": _pick(
                [
                    "Write clear README with problem and solution",
                    "Add screenshots and sample outputs",
                    "Show tech stack and design decisions",
                    "Include learning challenges and fixes",
                    "Keep code clean and versioned",
                ],
                5,
                ["README", "Screenshots", "Stack", "Challenges", "Clean code"],
            ),
        },
        "career_opportunities": {
            "salary": {
                "india_lpa": {
                    "fresher": _format_lpa(row.get("Salary_Fresher_Min_INR", ""), row.get("Salary_Fresher_Max_INR", ""), "3.0-6.0 LPA"),
                    "junior": _format_lpa(row.get("Salary_Junior_Min_INR", ""), row.get("Salary_Junior_Max_INR", ""), "5.0-10.0 LPA"),
                    "mid": _format_lpa(row.get("Salary_Mid_Min_INR", ""), row.get("Salary_Mid_Max_INR", ""), "8.0-16.0 LPA"),
                    "senior": _format_lpa(row.get("Salary_Senior_Min_INR", ""), row.get("Salary_Senior_Max_INR", ""), "13.0-24.0 LPA"),
                    "lead": _format_lpa(row.get("Salary_Lead_Min_INR", ""), row.get("Salary_Lead_Max_INR", ""), "20.0-40.0 LPA"),
                },
                "international": [
                    {
                        "country": "United States",
                        "entry": _format_currency(row.get("USA_Entry_Min_USD", ""), row.get("USA_Entry_Max_USD", ""), "USD", "USD 55,000-75,000"),
                        "mid": _format_currency(row.get("USA_Mid_Min_USD", ""), row.get("USA_Mid_Max_USD", ""), "USD", "USD 75,000-110,000"),
                        "senior": _format_currency(row.get("USA_Senior_Min_USD", ""), row.get("USA_Senior_Max_USD", ""), "USD", "USD 110,000-160,000"),
                    },
                    {
                        "country": "United Kingdom",
                        "entry": _format_currency(row.get("UK_Entry_Min_GBP", ""), row.get("UK_Entry_Max_GBP", ""), "GBP", "GBP 28,000-40,000"),
                        "mid": _format_currency(row.get("UK_Mid_Min_GBP", ""), row.get("UK_Mid_Max_GBP", ""), "GBP", "GBP 42,000-60,000"),
                        "senior": _format_currency(row.get("UK_Mid_Min_GBP", ""), row.get("UK_Mid_Max_GBP", ""), "GBP", "GBP 60,000-85,000"),
                    },
                ],
                "disclaimer": _translate(language, "Salary ranges vary by city, company, skills, and market conditions.", "சம்பள வரம்புகள் நகரம், நிறுவனம், திறன் மற்றும் சந்தை நிலைமைகளை பொறுத்து மாறும்."),
            },
            "top_hiring_companies": {
                "tech_giants": _pick(all_companies[0:3], 3, ["Amazon", "Microsoft", "Google"]),
                "indian_product": _pick(all_companies[3:6], 3, ["Flipkart", "Swiggy", "Razorpay"]),
                "it_services": _pick(all_companies[6:9], 3, ["TCS", "Infosys", "Wipro"]),
                "consulting": _pick(all_companies[9:10], 1, ["Deloitte"]),
            },
            "related_job_titles": _pick(
                [
                    _clean_text(row.get("Career_Path_Year_0_2", "")),
                    _clean_text(row.get("Career_Path_Year_3_5", "")),
                    _clean_text(row.get("Career_Path_Year_6_8", "")),
                    _clean_text(row.get("Career_Path_Year_9_Plus", "")),
                    _clean_text(row.get("Career_Path_Year_12_Plus", "")),
                    _clean_text(row.get("Career_Path_Year_15_Plus", "")),
                    _clean_text(row.get("Career_Path_Year_18_Plus", "")),
                    role,
                    f"Junior {role}",
                    f"Senior {role}",
                    f"Lead {role}",
                ],
                8,
                [role, f"Junior {role}", f"Senior {role}", f"Lead {role}"],
            ),
            "market_trend_indicator": {
                "trend": trend,
                "note": _translate(language, "Demand remains strong with consistent skill-based hiring.", "திறன் அடிப்படையிலான ஆட்சேர்ப்புடன் தேவை தொடர்ந்து உள்ளது."),
            },
            "application_strategy": _first_non_empty(
                [
                    row.get("Application_Strategy"),
                    _translate(language, "Apply consistently each week, tailor your resume to role keywords, and showcase practical projects.", "ஒவ்வொரு வாரமும் தொடர்ந்து விண்ணப்பிக்கவும், உங்கள் சுயவிவரத்தை பணியின் keyword-களுக்கு பொருத்தவும், நடைமுறை திட்டங்களை காட்டவும்."),
                ],
                "Apply consistently",
            ),
            "direct_apply_link": _resource_url(role, role, domain, "apply"),
        },
        "domain_role_catalog": _build_domain_role_catalog(rows, domain, role),
        "actions": {
            "save_progress": True,
            "resume_later": True,
            "export_pdf": True,
            "edit_inputs": True,
        },
        "ux_style_recommendation": {
            "layout": "Card-based clean layout",
            "navigation": "Sticky sidebar for quick navigation",
            "mobile": "Mobile-responsive blocks",
            "color_coding": [
                {"color": "Green", "meaning": "Strengths"},
                {"color": "Yellow", "meaning": "Improvement areas"},
                {"color": "Red", "meaning": "Risk areas"},
            ],
            "bilingual_labels": True,
        },
    }

    # Keep today relative references deterministic and date-bound.
    tomorrow = (today + timedelta(days=1)).isoformat()
    data["study_plan"]["today_task"]["tomorrow_preview"] = _translate(
        language,
        f"Tomorrow ({tomorrow}): continue with the next sub-topic and one timed practice.",
        f"நாளை ({tomorrow}): அடுத்த துணைத்தலைப்பை தொடர்ந்து ஒரு நேரமிட்ட பயிற்சியை செய்யவும்.",
    )

    return data
