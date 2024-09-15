from symbol import comparison

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#python function
total_score = sum(student_scores)
print(total_score)

# by looping
total = 0
for score in student_scores:
    total += score

print(total)

# python max

max = max(student_scores)
print(max)

# user defined

loop_max = 0

for score in student_scores:
    if score > loop_max:
        loop_max = score

print(loop_max)