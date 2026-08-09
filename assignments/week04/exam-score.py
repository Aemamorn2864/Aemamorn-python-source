# Assignment 2.1:โปรแกรมตรวจสอบผลการสอบ


scores = []

#รับคะแนนนักเรียน
for i in range(5):
    score = int(input(f"Enter score of student {i + 1}: "))
    scores.append(score)
print()

#ตรวจสอบ
for i in range(5):
    if scores[i] >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print(f"Student {i + 1}: {scores[i]} -> {result}")