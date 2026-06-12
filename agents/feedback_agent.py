from services.llm_service import LLMService


class FeedbackAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate_feedback(
        self,
        ats_score,
        matching,
        missing
    ):

        prompt=f"""
                You are an experienced AI recruiter.

                Candidate ATS Score:
                {ats_score}%

                Matching Skills:
                {", ".join(matching)}

                Missing Skills:
                {", ".join(missing)}

                Provide the following sections:

                Return your response in Markdown with these exact headings:

                ## Candidate Summary

                ## Strengths

                ## Weaknesses

                ## Hiring Recommendation

                Keep the response professional and concise.
                """

        return self.llm.generate(prompt)