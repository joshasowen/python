import random

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    
    while True:  
        question = input("Ask the Magic 8-Ball a question: ")
        if question.lower() == 'quit':  
            print("Goodbye!")
            break
        print("\nShaking the Magic 8-Ball...\n")
        print(random.choice(responses))
        print()  

magic_8_ball()