from main import time_taken

Students_score=0
Correct_answers=0
Incorrect_answers=0
Students_performance=[]

print(f"Time Taken:{time_taken}Seconds")
print(f"Students Score:{Students_score}")
print(f"Correct Answer:{Correct_answers}")
print(f"Incorrect Answer:{Incorrect_answers}")
Total_Questions=Correct_answers+Incorrect_answers
accuracy=(Correct_answers/Total_Questions)*100
print(f"Your Accuracy:{accuracy}%")