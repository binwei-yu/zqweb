from SI507_HW4 import *
import unittest
import csv
import numpy as np
import random
import itertools

class PartOne(unittest.TestCase):
    def test_movies_clean(self):
        self.cleaned_file = open('movies_clean.csv','r')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Title / first value in the row at index 1")
        self.assertTrue(self.row_reader[25].split(",")[0], "Testing that there is a Title / first value in the row at index 25")
        self.cleaned_file.close()

    def test_movies_clean_file2(self):
        cleaned_file = open('movies_clean.csv','r')
        self.contents = cleaned_file.readlines()
        cleaned_file.close()
        self.assertTrue("Three Kingdoms: Resurrection of the Dragon,0,22139590,20000000,03-Apr-08,R,NA,Based on Book/Short Story,Action,Historical Fiction,NA,NA\n" in self.contents, "Testing that the Three Kingdoms line exists correctly with formatted date & proper NAs in the clean file")
        self.assertTrue("51 Birch Street,84689,84689,350000,18-Oct-06,Not Rated,Truly Indie,NA,NA,NA,7.4,439\n" in self.contents, "Testing that 51 Birch Street line is correct in resulting file, including NAs, Not Rated preserved, etc")


class PartTwo(unittest.TestCase):
    def test_median_rating(self):
        self.assertEqual(median_rating, "PG-13", "Testing that median_rating has the correct value. NOTE that of course, hard-coding what you see on your screen is not acceptable here, even though we can't AUTOMATICALLY test your coding process -- you should write code to achieve this result; humans will look at submissions.")

class PartThree(unittest.TestCase):
    def test_sample_fake_movies1(self):
        self.assertTrue(len(sample_fake_movies.split("\n")) >= 10, "Testing that there are at least 10 lines in sample_fake_movies (note that other constraints will be tested manually by humans to assure full points on this question -- deductions may still occur if instructions were not followed)")

    def test_sample_fake_movies2(self):
        self.assertTrue( (len(sample_fake_movies.split("\n")[0]) <= 45) or (len(sample_fake_movies.split("\n")[0]).split() <= 9), "Testing that sample fake movies abides by constraints for length or word # in title")


if __name__ == "__main__":
    unittest.main(verbosity=2)
