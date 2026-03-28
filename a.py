# 답안의 key 기준으로 반복하는 방법
for key in correct_answer.keys():
    score = get_score(student[key], correct_answer[key])
    print(key, ": ",score)

# student key 기준으로 반복하는 방법
# for key in student.keys():
#     if key == 'name' or key == 'number':
#         continue
#     score = get_score(student[key], correct_answer[key])
#     print(key, ": ",score)