
class Teacher:

    def __init__(self, name, years, master_degree=False, topics=[]):
        self.name = name
        self.years_of_experience = years
        self.master_degree = master_degree
        self.topics = topics

    @property
    def amount_topics(self):
        return len(self.topics)

    @property
    def has_master_degree(self):
        return self.master_degree


class Director:
    pass