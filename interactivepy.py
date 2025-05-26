import pandas as pd

def main():
    df = pd.read_csv("interactive.csv")

    while True:
        option: str = input("which option: ")
        if option == "options":
            print("exit, options, topics, note")
        elif option == "topics":
            print(df.iloc[:,0])
        elif option == "note":
            choice: str = input("which note: ")
            print(df[df["topic"] == choice])
        elif option == "example":
            topic_choice: str = input("What topic: ")
            cpdf = df[df["topic"] == topic_choice]
            example = cpdf.iloc[:,2].str.split("/n")
            print(*example[0], sep="\n")
            i = len(example) - 1
            while i > 0:
                print(*example[i], sep="\n")
                i = i - 1
        elif option == "exit":
            break
        else:
            print("incorrect input, for options type options")


if __name__ == "__main__":
    main()
