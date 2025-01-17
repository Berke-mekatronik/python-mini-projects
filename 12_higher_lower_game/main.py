from art import logo
from art import vs
from game_data import data
import random

def game_reply(n1, n2):

    value_a = data[n1]['follower_count']
    print(f"Compare A: {data[n1]['name']}, a {data[n1]['description']}, {data[n1]['country']}")

    print(vs)

    value_b = data[n2]['follower_count']
    print(f"Compare B: {data[n2]['name']}, a {data[n2]['description']}, {data[n2]['country']}")

    empty_answer = ""
    if value_a > value_b:
        empty_answer = "a"
    else:
        empty_answer = "b"

    return empty_answer

score = 0
random_n1 = random.randint(0, len(data))
random_n2 = random.randint(0, len(data))
print(logo)
correct_answer = game_reply(random_n1, random_n2)
game_continue = True
while game_continue:
    if score < 1:
        pass
    else:
        print(f"You're right! Current score: {score}.")

    user_answer = input("Who has more followers? Type 'A' pr 'B': ").lower()

    print("\n" * 20)
    if user_answer == correct_answer:
        score += 1
        random_n1 = random_n2
        random_n2 = random.randint(0, len(data))
        correct_answer = game_reply(random_n1, random_n2)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False
