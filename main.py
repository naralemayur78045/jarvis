import webbrowser
import datetime

def jarvis():
    print("hello i am jarvis....")
    print("Avilable commands....")
    print("1.google")
    print("2.youtube")
    print("3.time")
    print("exit")

    while True:
        command = input("Enter the command: ").lower()

        if command == "google":
            print("opening google")
            webbrowser.open("https://www.google.com")

        elif command == "exit":
            break

        else:
            print("command not found")

jarvis()