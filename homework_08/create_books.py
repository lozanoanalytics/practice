""" Date: July 21, 2020 
@Author: Ivan Lozano
Filename: create_books.py
Purpose: Homework 8: working with dictionaries 
and for loops """

# An empty list, when the program first
# starts.  As the user starts to add 
# books, it will be filled with items --
# those items being dictionaries containing
# book information

books = []

choice = None

while choice != "0":
    print(
    """
    Create Books
    
    0 - Quit
    1 - List All Books
    2 - Add a Book
    3 - Delete a Book
    4 - Display Book Information
    """
    )
    choice = input("Choice: ")
    print()
    # exit
    if choice == "0":
        print("Good-bye.")
    # display books
    elif choice == "1":
        print("Books:\n")
        # This part of the program should print
        # each book's number (its index in the 
        # list) and its title
        # YOUR CODE STARTS HERE

        for i in range(len(books)):
            print (i, end = " : ")
            print (books[i]["title"])

        # YOUR CODE ENDS HERE

    # add a book
    elif choice == "2":
        # This part of the program should:
        #   -Create an empty dictionary
        #   -Add keys to the dictionary for 
        #       title
        #       author
        #       year
        #       pages
        #    while getting the values through
        #    user input. (Here, "year" means 
        #    the year of publication.)
        #   -Append the newly-filled dictionary
        #    to the list books
        # YOUR CODE STARTS HERE
        books_dict = {}

        books_dict["title"] = input ("What is the title?: ")
        books_dict["author"] = input ("What is the author?: ")
        books_dict["year"] = input ("Year of Publication?: ")
        books_dict["pages"] = input ("How many pages? ")

        books.append(books_dict)
        print()
        print("Added " + books_dict["title"])
        # YOUR CODE ENDS HERE

    # delete a book
    elif choice == "3":
        # This part of the program should:
        #   -List the numbers and titles
        #    for the books currently in 
        #    the system.  For this part, you
        #    can reuse the code from choice 
        #    number 1 above.
        #   -Get the number for the book 
        #    from the user, converted to int
        #   -Use the number as the INDEX to 
        #    delete the item from the list books

        # YOUR CODE STARTS HERE
        print("Books:\n")
        # This part of the program should print
        # each book's number (its index in the 
        # list) and its title
        # YOUR CODE STARTS HERE

        for i in range(len(books)):
            print (i, end = " : ")
            print (books[i]["title"])

        print()

        remove_book = int(input("Which number book do you want?: " ))
        print ("Deleted " + str(books[remove_book]["title"]))
        del books[remove_book]
        
        # YOUR CODE ENDS HERE

    # print info about a book
    elif choice == "4":
        # This part of the program should:
        #   -List the numbers and titles
        #    for the books currently in 
        #    the system.  For this part, you
        #    can reuse the code from choice 
        #    number 1 above.
        #   -Get the number for the book 
        #    from the user, converted to int
        #   -Use the number as the INDEX to 
        #    get the item from the list books
        #   -That item will be a dictionary. For 
        #    each key in the dictionary, print:
        #       *The key
        #       *Its corresponding value

        # YOUR CODE STARTS HERE

        for i in range(len(books)):
            print (i, end = " : ")
            print (books[i]["title"])
        
        print()

        book_info = int(input("Which number book do you want?: " ))
        books_dict = books[book_info]

        print ()

        for key in books_dict.keys():
            print(key + " : " + books_dict[key])

        # YOUR CODE ENDS HERE

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
    print()