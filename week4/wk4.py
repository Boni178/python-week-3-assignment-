
#FILE HANDLING CODE
with open ("week4/file.txt",  "r") as file:
     data = file.read()

     with open ("week4/file.txt",  "a") as file:
       data = file.write( "AWESOME")



with open("week4/file.txt", "r") as file:
    modified_data = file.read()


print(modified_data)


#ERROR HANDLING CODE

userINPUT = input("Enter your file name: ")

try:
    with open(userINPUT, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the filename.")
