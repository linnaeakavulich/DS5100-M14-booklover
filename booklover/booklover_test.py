import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):  
        # add a book and test if it is in `book_list.
        new = BookLover('Linnaea', 'linnaeakavulich@gmail.com', 'Nonfiction')
        new.add_book('Plato\'s Republic', 4)
        self.assertTrue('Plato\'s Republic' in list(new.book_list['book_name']))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        new = BookLover('Linnaea', 'linnaeakavulich@gmail.com', 'Nonfiction')
        new.add_book('Plato\'s Republic', 4)
        new.add_book('Plato\'s Republic', 4)
        double_add = new.book_list[new.book_list['book_name'] == 'Plato\'s Republic']
        self.assertTrue(len(double_add) == 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        new = BookLover('Linnaea', 'linnaeakavulich@gmail.com', 'Nonfiction')
        new.add_book('Plato\'s Republic', 4)
        self.assertTrue(new.has_read('Plato\'s Republic') == True)
    
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True
        new = BookLover('Linnaea', 'linnaeakavulich@gmail.com', 'Nonfiction')
        new.add_book('Plato\'s Republic', 4)
        self.assertFalse(new.has_read('Harry Potter') == True)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        new = BookLover('Linnaea', 'linnaeakavulich@gmail.com', 'Nonfiction')
        new.add_book('Plato\'s Republic', 4)
        new.add_book('Little Women', 2)
        new.add_book('A Series of Unfortunate Events', 5)
        
        total_num = [new.num_books_read]
                
        self.assertTrue(len(total_num) == 3)
    
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        # add some books to the list, and test num_books matches expected.
        new = BookLover('Linnaea', 'linnaeakavulich@gmail.com', 'Nonfiction')
        new.add_book('Plato\'s Republic', 4)
        new.add_book('Little Women', 2)
        new.add_book('A Series of Unfortunate Events', 5)
        
        new_list = [new.fav_books()]
        self.assertFalse('Little Women' in new_list)
                    
            
if __name__ == '__main__':
    unittest.main(verbosity=3)