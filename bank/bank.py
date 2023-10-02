greetings = input("Greetings: ").lower().strip()

if greetings.startwith("hello"):
    print("$0")
elif greetings.startswith("h"):
    print("$20")
else:
    print("$100")