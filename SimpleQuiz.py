def take_quiz():
  """Conducts a simple multiple-choice quiz"""

  # Define questions and answer keys
  questions = [
    "What is the capital of France? (a) Paris, (b) London, (c) Berlin",
    "What is the largest planet in our solar system? (a) Earth, (b) Jupiter, (c) Mars",
  ]
  answer_keys = ["a", "b"]
  score = 0

  # Present questions and get user answers
  for i, question in enumerate(questions):
    print(f"\nQuestion {i+1}: {question}")
    answer = input("Enter your answer (a, b, or c): ").lower()
    if answer == answer_keys[i]:
      score += 1
      print("Correct!")
    else:
      print("Incorrect. The correct answer is", answer_keys[i])

  # Calculate and print the results
  total_questions = len(questions)
  print(f"\nYou scored {score} out of {total_questions} questions.")

# Run the quiz
take_quiz()
