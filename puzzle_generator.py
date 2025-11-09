import random
def generate_question(level):
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"{a} + {b}"
        answer = a + b
    elif level == "Medium":
        a, b = random.randint(5, 40), random.randint(1,25)
        ops = random.choice(["+", "-", "*"])
        question = f"{a} {ops} {b}"
        answer = eval(question)
    elif level == "Hard":
      a, b, c = random.randint(5, 15), random.randint(2, 10), random.randint(1, 5)
      div=random.choice(["*","//"])
      question = f"({a} {div} {b}) + {c}"
      answer = (a * b) + c
    return question, answer