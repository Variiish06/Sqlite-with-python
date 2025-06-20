def main():
    while True:
        user_input = input("db> ").strip()
        if user_input == ".exit":
            print("Exiting...")
            break
        else:
            print("Unrecognized input:", user_input)

if __name__ == "__main__":
    main()
