import pandas as pd

def main():
    df = pd.read_csv("interactive.csv")

    while True:
        option = input("which option: ")
        if option == "options":
            print("exit, options, topics, note")
        elif option == "topics":
            print(df.iloc[:,0])
        elif option == "note":
            choice = input("which note: ")
            print(df[df["topic"] == choice])
        elif option == "exit":
            break
        else:
            print("incorrect input, for optiopns type options")


if __name__ == "__main__":
    main()
