subject_score = {'65010001':{'python':30}}
new = {}
student = input()
subject = input()
score = int(input())
def add_score(subject_score,student,subject,score):
    if subject_score.get(student):
        subject_score[student].update({subject:score})
    else:
        subject_score.update({student:{subject:score}})
    return print(subject_score)
def calc_average_score(subject_score):
    new = {}
    sumx = 0
    sumy = 0
    # for student,subject in subject_score.items():
        # print(student)
        # print(subject)

    #   sumx += subject.values()
    #   sumy += 1
    #   new.update({student:"{:.2f}".format(sumx/sumy)})
    # return new
add_score(subject_score,student,subject,score)
calc_average_score(subject_score)
