import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list


    def add_book(self, book_name, book_rating):
        if book_name in list(self.book_list['book_name']): 
            print('You already have this title!')
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            return self.book_list
       
        
    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            print('You\'ve read this book!')
            return True
        else:
            return False
        

    def num_books_read(self):
        books_read = len(self.book_list['book_name'])
        print(books_read)
        

    def fav_books(self):
        fav_books = self.book_list[self.book_list['book_rating'] >= 3]
        print(fav_books)