class ATSScore:

    @staticmethod
    def calculate(matching_skills, jd_skills):

        if len(jd_skills) == 0:
            return 0

        score = (
            len(matching_skills)
            / len(jd_skills)
        ) * 100

        return round(score, 2)
