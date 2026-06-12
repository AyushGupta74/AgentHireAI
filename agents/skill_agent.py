from services.llm_service import LLMService


class SkillAgent:

    def __init__(self):

        self.llm = LLMService()

    def detect_skills(self, text):

        prompt = f"""
                You are an AI skill extraction system.

                Extract ONLY technical skills, programming languages,
                frameworks, libraries, databases, cloud platforms,
                tools and technologies.

                Ignore education, locations, companies,
                soft skills and job titles.

                Return ONLY a comma-separated list.

                Text:

                {text}
                """

        response = self.llm.generate(prompt)

        skills = [
            skill.strip().lower()
            for skill in response.split(",") # type: ignore
            if skill.strip()
        ]

        return list(set(skills))