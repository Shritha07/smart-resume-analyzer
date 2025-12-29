import re
from skills_db import SKILL_ALIASES

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()

def extract_skills(text):
    words = normalize(text)
    found = set()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias in words:
                found.add(skill)
    return found

def analyze_resume(resume, job_desc):
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_desc)

    matched = resume_skills & job_skills
    missing = job_skills - resume_skills

    score = int((len(matched) / max(len(job_skills), 1)) * 100)

    reasons = {
        skill: f"Employers expect {skill} for this role based on industry standards."
        for skill in missing
    }

    return {
        "score": score,
        "matched": sorted(matched),
        "missing": sorted(missing),
        "reasons": reasons
    }
