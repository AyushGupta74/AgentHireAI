from models.matcher import ResumeMatcher


class MatchingAgent:

    def __init__(self):

        self.matcher = ResumeMatcher()

    def analyze(self, resume_text, jd_text):

        score = self.matcher.calculate_match_score(
            resume_text,
            jd_text
        )

        return score
