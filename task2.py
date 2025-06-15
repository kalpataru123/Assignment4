n1=input("Enter text to write to the file: ");
with open("output.txt","w") as file:
    file.write(str(n1+"\n"));
    print("data successfully writen to 'output.txt'");
n2=input("\nEnter additional text to append:");
with open("output.txt","a") as file:
    file.write(str(n2));
    print("data successfully appended");
print("\nfinal content of output.txt: ");
with open("output.txt","r") as file:
    data=file.read();
    print(data);