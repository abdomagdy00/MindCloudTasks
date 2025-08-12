
# Task1: Chat Bot

user_data={}
bot_name="Chat Bot"

print(f"\t\t\tHello I am '{bot_name}' :) ")
while True:
    user_input=input("You:")
    user_input_lower = user_input.lower().strip()

    if user_input_lower in ["exit", "quit", "bye", "stop"]:
        print(f"{bot_name}: Goodbye! Have a great day.")
        break

    if "name" not in user_data:
        if "hello" in user_input_lower or "hi" in user_input_lower:
            print(f"{bot_name}: Hello! I'm {bot_name}. What's your name?")
            user_data['name'] = input("You: ")
            print(f"{bot_name}: Nice to meet you, {user_data['name']}!")
            continue

    if "hello" in user_input_lower or "hi" in user_input_lower:
        if 'name' in user_data:
            print(f"{bot_name}: Hello again, {user_data['name']}!")
        else:
            print(f"{bot_name}: Hello there!")
        continue

    if "+" in user_input_lower:
        try:
            numbers_str = user_input.split('+')
            num1 = float(numbers_str[0].strip())
            num2 = float(numbers_str[1].strip())
            result = num1 + num2
            print(f"{bot_name}: The result is {result}")
        except (ValueError, IndexError):
            print(f"{bot_name}: It looks like you entered an invalid math operation. Please use a format like: 5+3")
        continue

    if "-" in user_input_lower:
        try:
            numbers_str = user_input.split('-')
            num1 = float(numbers_str[0].strip())
            num2 = float(numbers_str[1].strip())
            result = num1 - num2
            print(f"{bot_name}: The result is {result}")
        except (ValueError, IndexError):
            print(f"{bot_name}: It looks like you entered an invalid math operation. Please use a format like: 10-2")
        continue

    if "*" in user_input_lower:
        try:
            numbers_str = user_input.split('*')
            num1 = float(numbers_str[0].strip())
            num2 = float(numbers_str[1].strip())
            result = num1 * num2
            print(f"{bot_name}: The result is {result}")
        except (ValueError, IndexError):
            print(f"{bot_name}: It looks like you entered an invalid math operation. Please use a format like: 2*5")
        continue

    if "/" in user_input_lower:
        try:
            numbers_str = user_input.split('/')
            num1 = float(numbers_str[0].strip())
            num2 = float(numbers_str[1].strip())
            result = num1 / num2
            print(f"{bot_name}: The result is {result}")
        except (ValueError, IndexError):
            print(f"{bot_name}: It looks like you entered an invalid math operation. Please use a format like: 10/2")
        continue

    print(f"{bot_name}: I'm sorry, I don't understand what you're saying. Can you rephrase that?")


