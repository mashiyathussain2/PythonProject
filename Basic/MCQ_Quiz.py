class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "How do you start writing a for loop in Python?\n(a) for x in y:\n(b)for x > y:\n",
     "Are nested if-else are allowed in python?\n(a) Yes\n(b)No\n",
     "Which of the following is an invalid variable?\n(a) my_string_1\n(b)1st_string\n",
     "Which method can be used to replace parts of a string?\n(a) replace()\n(b)repl()\n",
     "How do you insert COMMENTS in Python code?\n(a) /*This is a comment*/\n(b) #This is a comment\n",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
