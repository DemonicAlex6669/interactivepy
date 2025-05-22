include pandas as pd

Def main():
    df = pd.read_csv("interactive.csv")

    while option != "quit":
       option = input("which option: ")
        if option == "options":
            print("quit, options, topics, note")
        elif option == "topics":
            print(df[0])
        elif option == "note":
            choice = input("which note: ")
            if df["topic"] == choice: #if choice in note object
                print(df[df["topic"] == choice])
        else:
            print("incorrect input, for optiopns type options")


If __name__ == "__main__":
    main()
