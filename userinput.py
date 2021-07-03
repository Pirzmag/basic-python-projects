responses = {}

poll_active = True

while poll_active:
    name = input("What's your name? ")
    response = input("\nWhere would you like to go? ")

    responses[name] = response

    stop = input("\nIs there another person? (y/n) ")
    if stop == 'n':
        poll_active = False

for name, place in responses.items():
    print(f"{name.title()} wants to go to {place}")
