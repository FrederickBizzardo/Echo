import wikipedia
import pyttsx3

engine = pyttsx3.init()

answer = "y"

print("Echo! A searching AI\n"
      "====================")
print("P.S: Don't forget to turn up your volume!\n")
while answer == "y":
    search = input('Search something: ')

    print(wikipedia.summary(f"{search}"))
    engine.say(wikipedia.summary(f"{search}"))
    engine.runAndWait()

    answer = input("Do you want to continue? [ y/n ]")
    if answer != "y":
        print("End of application\n"
              "==================")
