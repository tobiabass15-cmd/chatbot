import random
username = "selene"
password = "1234"
def login():
    while True:
        print("enter your username")
        user_name = input()

        print("enter your password")
        pass_word = input()
        if user_name == username and pass_word == password:
            print("login successfull")
            main_menu()
            return
        else:
            print("Invalid credentials")
def snack_convo():
    print("Lets talk about snacks!")

    snack = input("What is your favourite snack? ")
    print(snack, "sounds very tasty!")

    print("Do you like sweet snacks or salty snacks?")
    choice = input().lower()

    if choice == "sweet":
        print("Nice! Chocolates and cakes are yummy!")
    elif choice == "salty": 
        print("Chips and Popcorn are good!")
    else :
        print("Interesting Choice!")
def movie_convo() :
    print("Lets talk about some movies!")
    name = input("But tell me, what is your name.")
    print("Hi there", name)
    movie = ['spiderman', 'ironman', 'thor', 'batman', 'superman']
    print("do you like movies")
    ans = input().lower()
    if ans == "yes" :
        print("Nice, i like them to!")
    elif ans == "no" :
        print("Aw man, you should try some.")
    else :
        print("Invalid.")
def conversation_menu() :
    print("\nWhat do you want to talk about")
    print("1. Movies")
    print("2. Snacks")
    choicee = int(input("enter your choice, 1 or 2"))
    if choice == 1 :
        movie_convo()
    elif choice == 2 :
        snack_convo()
    else :
        print("Invalid Choice")
def guessing_game() :
    guess = int(input("Enter a number between one and 10"))
    num = random.randint(1,10)
    if guess == num :
        print("congrats!")
    else :
        print("Nope.")
        print(num)
def mind_game() :
    import time
    import random
    print("think of a number between 1 through 10 and dont tell anyone.")
    time.sleep(5)
    print("take the same amount as a loan from your parents. Type yes when done.")
    answer = input("")
    if answer == "yes" :
        print("ok, lets move on.")
    myamount = [10, 12, 14, 16, 18, 20]
    myamountchoice = random.choice(myamount)
    print("Now, add", myamountchoice, "in the amount in your mind.")
    time.sleep(4)
    print("Now give half the amount to your friend.")
    time.sleep(4)
    print("return the loan you took from your parents.")
    print("if you are done, type yes.")
    ans = myamountchoice/2
    answer = input("")
    if answer == "yes" :
        print("The answer in your mind is", ans)
def calculator():
    num1 = int(input("enter 1st num: "))
    num2 = int(input("enter 2nd num: "))

    print("Choose operation (Type the sign: + or - or * or /)")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

    choice = input("enter your choice: ")

    if choice == '+':
        print("Result:", num1 + num2)
    elif choice == '-':
        print("Result:", num1 - num2)
    elif choice == '*':
        print("Result:", num1 * num2)
    elif choice == '/':
        if num2 == 0:
            print("Division by zero not allowed")
        else:
            print("Result:", num1 / num2)
    else:
        print("invalid choice")
def rectangle(choice):
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    if choice == 1:
        print("Area of rectangle:", length * width)
    elif choice == 2:
        print("Perimeter of rectangle:", 2 * (length + width))
def square(choice):
    side = float(input("Enter side: "))

    if choice == 1:
        print("Area of square:", side * side)
    elif choice == 2:
        print("Perimeter of square:", 4 * side)
def circle(choice) :
    radius = float(input("enter radius:"))
    
    if choice == 1 :
        print("Area of circle:", 3.14 * radius * radius)
    elif choice == 2 :
        print("Perimeter of circle :",  2 * 3.14 * radius)
        
def math_formula():
    print("\n--- Geometry Calculator ---")
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Square")

    shape = int(input("Enter your choice (1-2): "))

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Perimeter")
    choice = int(input("enter your choice. 1 or 2"))
    if shape == 1 :
        rectangle(choice)
    elif shape == 2 :
        square(choice)
    else :
        print("Invalid choice")
def quiz_mode() :
    print("\n---Quiz Mode---")    
    score = 0
    questions = [
        "what is the correct file extension for python?",
        "which keyword is used to define a function?",
        "which symbol is used for comments in python?",
        "what does input() do? ",
        "which loop runs again and again until condition is false?"
        ]
    options = [
        [".py", ".java", ".html", ".txt"],
        ["define", "func", "def", "function"],
        ["//", "#", "/", "--"],
        ["Prints output", "Takes user input", "Stops program", "defines varible"],
        ["for", "while", "if", "elif"]
        ]
        answers = [1, 3, 2, 2, 2]
    for i in range(len(questions)):
        print("\nQ", i + 1, ";", questions[i])
        for j in range(len(options[i])) :
            print(j + i, ".", options[i][j])
        user_ans = int(input("enter your answer (1-4"))
        if user_ans == answers[i] :
            print("correct")
            score = score + 1
        else :
            print("wrong")
        print("\nQuiz Finsished!")
        print("your score: ", score, "/", len(questions))
def km_to_meter(km) :
    return km * 1000
def meter_to_km(meter) :
    return meter / 1000
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
def hour_to_minute(hour):
    return hour * 60
def minute_to_hour(minute):
    return minute / 60
def unit_converter():
    print("\n---Unit Converter---")
    print("1.Kilometer to Meter")
    print("2.Meter to Kilometer")
    print("3. Fahrenheit to Celsius")
    print("4. Celsius to Fahrenheit")
    print("5. Hour to Minute")
    print("6.Minute to Hour")
    choice = int(input("Enter choice (1-6)"))
    if choice == 1 :
        km = float(input("enter kilometers:"))
        print("meters:", km_to_meter(km))
    elif choice == 2 :
        meter = float(input("Enter meters:"))
        print("Kilometers:", meter_to_km(meter))
    elif choice == 3 :
        f = float(input("enter fahrenheit"))
        print("celsius :", fahrenheit_to_celsius(f))
    elif choice == 4 :
        c = float(input("enetr celsius"))
        print("fahrenheit :", celsius_to_fahrenheit(c))
    elif choice == 5 :
        hour = float(input("Enter hours"))
        print("minutes :", hour_to_minute(hour))
    elif choice == 6 :
        minute = float(input("Enter minutes"))
        print("Hours :", minute_to_hour(minute))
    else :
        print("invalid")
import random
def rps_game() :
    print("rock paper scissors game.")
    print("lets start!")
    options = ["rock", "paper", "scissors"]
    while True :
        user_choice = input("enter your choice ;\n").lower()
        print("your choice:", user_choice)
        if user_choice not in options:
            print("Invalid choice")
            continue
        computer_choice = random.choice(options)
        print("Computer chose", compter_choice)
        if user_choice == computer_choice :
            print("its a tie")
        elif user_choice == "rock" and computer_choice == "scissors" :
            print("you win!")
        elif user_choice == "scissors" and computer_choice == "paper" :
            print("you win!")
        elif user_choice == "paper" and computer_choice == "rock" :
            print("you win")
        else :
            print("computer wins")
  
main_menu()