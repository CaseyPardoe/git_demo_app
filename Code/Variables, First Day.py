#print ('Hello World')

#name = input('please enter your name ')
#age = input('please enter your age casey')
#print(f'your name is {name} and your age is {age}')

#length = int(input('please enter the length of the rectangle '))
#width = int(input('please enter the width of the rectangle '))
#perimeter = (length * 2 + width * 2)
#area = (length * width)

#print(f'the perimeter of your rectangle is {perimeter}')
#print(f'the area of your rectangle is {area}')


dict = {"Oscar Wilde": ["The Picture of Dorian Gray", 
                        "The Importance of Being Earnest"],
                                                             "J.R.R. Tolkien": ["The Hobbit", 
                                                                                "The Fellowship of the Ring"] }
#new_author = input("please enter a new author ")
#new_book = input("please enter a book by this author ")
#x = ", ".join(dict)

#dict.update({new_author: [new_book]})

author_query = input("please choose an author ")

print(dict.get((author_query)))

#print(x)