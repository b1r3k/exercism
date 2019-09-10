class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sorted_scores = sorted(scores, reverse=True)

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return self.sorted_scores[0]

    def personal_top(self):
        return self.sorted_scores[0:3]

    def report(self):
        msg = "Your latest score was %s." % self.latest()
        if self.latest() >= self.personal_best():
            msg += " That's your personal best!"
        else:
            msg += " That's %d short of your personal best!" % (self.personal_best() - self.latest())
        return msg
