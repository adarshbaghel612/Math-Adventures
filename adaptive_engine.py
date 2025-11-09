Difficulty=["Easy","Medium","Hard"]
difficulty="Medium"
Students_score=0
def Adaptive_engine():
    if Students_score>=2 and difficulty !="Hard":
        current_difficulty=Difficulty.index(difficulty)
        increased_difficulty=Difficulty[current_difficulty+1]
        difficulty=increased_difficulty
        Students_score=0
        print(f"Difficulty Increased to {increased_difficulty}")
    elif Students_score<=-2 and difficulty !="Easy":
        current_difficulty=Difficulty.index(difficulty)
        decreased_difficulty=Difficulty[current_difficulty-1]
        difficulty=decreased_difficulty
        Students_score=0
        print(f"Difficulty Decreased to {decreased_difficulty}")