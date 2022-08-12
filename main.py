books = []

with open ("books.txt") as textFile:
    for line in textFile:
        book = [item.strip() for item in line.split(',')]
        books.append(book)


library = {}

books.sort()

for book in books:
    if book[-1] in library.keys():
        library[book[-1]].append(book[0])
    else:
        library[book[-1]] = [book[0]]
        
b = True
while (b):
    count = 0
    for key in library.keys():
        count += 1
        print (str(count) + ". " + key)
        
    choice = input("Select which genre of book you would like to checkout via number 1 - " + str(count) + ":  ")    
    genre = list(library.keys())[(int(choice) - 1)]
    print(library[genre])
    cont = input("Would you like to look at another genre? Y/N:  ")
    if cont == "N":
        print("Thank you for visiting the library")
        b = False
    
