class Note:
    def __init__():
        self._this = ...
        self._topic = ...
        self._name = ...
        self._code = ...
        self._additional = ...
        self__notes = ...
        self._interactive = ... #add specific symbol where to input text, so a latter method can let you type there
    def ...:
        ...


Def main():
    topics = []
    notes = [] #list of note objects

    ...
    topics += self._topic

    option = input("which option: ")
    while option != "quit":
        if option == "options":
            ...
        elif option == "topics":
            print(f"{topics}")
        elif option == "note":
            choice = input("which note: ")
            if choice ...: #if choice in note object
                print(...)
        else ...:
            ...
        option = input("which option: ")


If __name__ == "__main__":
    main()
