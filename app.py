import streamlit as st

from agents.parser_agent import ResumeParserAgent
from agents.skill_agent import SkillAgent
from agents.comparison_agent import ComparisonAgent
from models.ats_score import ATSScore
from agents.feedback_agent import FeedbackAgent

st.title("AgentHire AI")
st.caption("AI-powered Resume Screening & Recruitment Assistant")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file is None:

        st.warning("Please upload a resume.")

    elif job_description.strip() == "":

        st.warning("Please paste a job description.")

    else:

        parser = ResumeParserAgent()

        resume_text = parser.parse_resume(
            uploaded_file
        )

        skill_agent = SkillAgent()

        skills = skill_agent.detect_skills(
            resume_text
        )
        comparison = ComparisonAgent()

        matching, missing, jd_skills = comparison.compare(
            resume_text,
            job_description.lower()
        )

        score = ATSScore.calculate(
            matching,
            jd_skills
        )

        st.success("Analysis Complete!")

        st.metric(
            "ATS Match Score",
            f"{score}%"
        )

        st.subheader("Matching Skills")

        for skill in matching:
            st.write(f"{skill.title()}")

        st.subheader("Missing Skills")

        if len(missing) == 0:
            st.success("No missing skills found!")
        else:
            for skill in missing:
                st.error(skill.title())

        st.subheader("Resume Skills")

        for skill in matching:
            st.success(skill.title())

        st.divider()

        with st.spinner("Generating AI feedback..."):

            feedback_agent = FeedbackAgent()

            feedback = feedback_agent.generate_feedback(
                score,
                matching,
                missing
            )

        st.subheader("AI Recruiter Feedback")

        st.markdown(feedback)