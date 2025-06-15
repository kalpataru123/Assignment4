try:
    with open("sample.txt","r") as file:
        print("Reading file content:");
        for line in file:
            print(line.strip());
except FileNotFoundError:
    print("the file '{sample.txt}' are not found.");