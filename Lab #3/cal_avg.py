subject_score = {'python':30}
subject = input()
score = int(input())
def add_score(subject_score,subject,score):
    subject_score[subject] = score
    return subject_score
def calc_average_score(subject_score):
   x = sum(subject_score.values())
   y = len(subject_score.keys())
   "{:.2f}".format(x/y)
   return print(str(x/y))
#subject_score.get()
add_score(subject_score,subject,score)
calc_average_score(subject_score)
