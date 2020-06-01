# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 08:50:03 2020

@author: quinn
"""
import unittest

import CA1_Markets

class testCA1(unittest.TestCase):
    #Steup
    def set_up(self):
        pass
    #Confirm content
    def test_market_scrape(self):
        self.assertTrue(len(CA1_Markets.market_scrape()) >0)
    #Test column size is 4
    def test_table_data(self):
        B_S = CA1_Markets.market_scrape()
        self.assertEqual(len(B_S) ,4)
    #Confirm size is not above 4
    def test_table_size(self):
        B_S = CA1_Markets.market_scrape()
        self.assertGreater(len(B_S) ,5)


if __name__ == '__main__':
    unittest.main()

