import random

def generate_quote():
    quotes = [
        "The best way to predict the future is to invent it.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "Do not wait to strike till the iron is hot; but make it hot by striking.",
        "Success usually comes to those who are too busy to be looking for it.",
        "The journey of a thousand miles begins with one step."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Here is a random quote for you:")
    print(generate_quote())
