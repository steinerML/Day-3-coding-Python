# We take input from user as an integer

score = int(input("Enter your exam result: "))

if score >= 100 :
    print("Score is not valid")

elif score >= 50 :
    print("Congratulations! You passed the exam")
else :
    print("Sorry, you have failed miserably!")
