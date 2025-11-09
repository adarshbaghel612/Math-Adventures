from puzzle_generator import generate_question
from adaptive_engine import Adaptive_engine
import time
Students_score=0
Correct_answers=0
Incorrect_answers=0
Students_performance=[]

Students_name=input("Enter Your Name:")
print(f"Welcome {Students_name}")

Difficulty=["Easy","Medium","Hard"]
difficulty=input("Enter your desired Difficulty:")
while True:
    question, answer=generate_question(difficulty)
    print(f"Question:{question}")
    start_time=time.time()
    Students_answer=int(input("Your Answer:"))
    if Students_answer==answer:
        print("Correct Answer")
        Students_score+=1
        Correct_answers+=1
    else:
        print(f"Incorrect Answer.Correct Answer is {answer}")
        Students_score-=1
        Incorrect_answers+=1
    end_time=time.time()
    time_taken=end_time-start_time
    print(f"Time Taken:{time_taken}Seconds")

    if Students_score>=2 and difficulty !="Hard":
            current_difficulty=Difficulty.index(difficulty)
            increased_difficulty=Difficulty[current_difficulty+1]
            difficulty=increased_difficulty
            Students_score=0
            print(f"Difficulty Increased to {increased_difficulty}")
    elif Students_score<=-2 and difficulty !="Easy":
            current_difficulty=Difficulty.index(difficulty)
            decreased_difficulty=Difficulty[current_difficulty-1]
            Students_score=0
            print(f"Difficulty Decreased to {decreased_difficulty}")
    if Students_answer==000:
      break
print("Here is your Quiz Summary:")
print(f"Students Score at current difficulty level:{Students_score} ")
print(f"Correct Answer:{Correct_answers}")
print(f"Incorrect Answer:{Incorrect_answers}")
Total_Questions=Correct_answers+Incorrect_answers
accuracy=(Correct_answers/Total_Questions)*100
print(f"Your Accuracy:{accuracy}%")
if accuracy>70:
    print("You are doing Good")
else:
     print("Keep on Practicing.Good Luck!")
    