from django.shortcuts import render
from .pdf_reader import extract_text_from_pdf
from .ai_engine import find_skills, calculate_match
from .nlp_engine import calculate_similarity


def home(request):

    extracted_text = ""
    skills = []
    score = 0
    ai_score = 0
    matched_skills = []
    missing_skills = []

    if request.method == "POST":

        resume = request.FILES.get("resume")
        job_description = request.POST.get("job_description")

        if resume:

            extracted_text = extract_text_from_pdf(resume)

            skills = find_skills(extracted_text)

            score, matched_skills, missing_skills = calculate_match(
                skills,
                job_description
            )

            ai_score = calculate_similarity(
                extracted_text,
                job_description
            )

    return render(
        request,
        "analyzer/home.html",
        {
            "extracted_text": extracted_text,
            "skills": skills,
            "score": score,
            "ai_score": ai_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }
    )