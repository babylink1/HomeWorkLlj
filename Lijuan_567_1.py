"""
    Author: LiuLijuan
    Course: 2023S-SSW567-WS
    Assignment: Lijuan_567_1
    Date & Time: Tue Sep 12 23:45
"""

import unittest
  
def my_brand(name):
   print(name)
   return name
   
def main():
    
    my_brand("LiuLijuan")
    
    print("Hello world")
    
main()
    
class MyBrandTestCase(unittest.TestCase):
    def test_my_brand(self):
        
        self.assertEqual(my_brand("LiuLijuan"), "LiuLijuan")
       

unittest.main()
