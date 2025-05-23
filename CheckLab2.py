#!/usr/bin/env 

import subprocess
import unittest
import sys
import os

class lab2a(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2a.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2a.py'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        self.assertEqual(out, b'Hi Jon, you are 20 years old.\n')

class lab2b(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2b.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        out, _ = p.communicate(b'Jon\n20\n')
        self.assertEqual(out, b'Name: Age: Hi Jon, you are 20 years old.\n')

class lab2c(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2c.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2c.py', 'Jon', '20'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        self.assertEqual(out, b'Hi Jon, you are 20 years old.\n')

class lab2d(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2d.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2d.py', 'Jon', '20'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        self.assertEqual(out, b'Hi Jon, you are 20 years old.\n')

class lab2e(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2e.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2e.py'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        self.assertEqual(out, b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n')

class lab2f(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2f.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2f.py', '5'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        self.assertEqual(out, b'5\n4\n3\n2\n1\nblast off!\n')

class lab2g(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists('lab2g.py'))
    def test_output(self):
        p = subprocess.Popen([sys.executable, 'lab2g.py', '3'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        self.assertEqual(out, b'3\n2\n1\nblast off!\n')

if __name__ == '__main__':
    unittest.main()
