from collections import namedtuple, defaultdict

Grade = namedtuple('Grade', ('score','weight'))

class Subjects:
    def __init__(self):
        self._grades = []

    def add_subject(self,score,weight):
        self._grades.append(Grade(score, weight))

    def get_sum(self):
        total = 0
        for each_grade in self._grades:
            total += each_grade.score
        return total

class Subject:
    def __init__(self):
        self._subject = defaultdict(Subjects)

    def get_subject(self,subject_name):
        return self._subject[subject_name]

    def check_subject(self,subject_name,score,weight):
        self._subject[subject_name].add_subject(score,weight)


class Name:
    def __init__(self):
        self._name = defaultdict(Subject)

    def get_name(self, name):
        return self._name[name]

name = Name()
dinesh = name.get_name('Dinesh')
get_subject = dinesh.get_subject('Math')
get_subject.add_subject(50, 0.45)
get_subject.add_subject(45, 0.35)

print(get_subject.get_sum())





