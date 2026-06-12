from agents.skill_agent import SkillAgent


class ComparisonAgent:

    def __init__(self):
        self.skill_agent = SkillAgent()

    def compare(self, resume_text, jd_text):

        resume_skills = set(
            self.skill_agent.detect_skills(resume_text)
        )

        jd_skills = set(
            self.skill_agent.detect_skills(jd_text)
        )

        matching = sorted(
            resume_skills.intersection(jd_skills)
        )

        missing = sorted(
            jd_skills - resume_skills
        )

        return matching, missing, jd_skills
