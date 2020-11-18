import unittest
import os
import sys
import numpy
sys.path.append('../')
from faceDetection import FaceRecognition

class TestFace(unittest.TestCase):
    new_dir = "../new_faces/"
    known_dir = "../known_faces/"
    cam1 = FaceRecognition(1)
    
    def setUp(self):
        pass
    
    def tearDown(cls):
        pass
        #os.rename("../known_faces/0001.jpg","../new_faces/0001.jpg")

    def test_encoding(self):
        result = self.cam1.generate_faceEncode('0001',self.new_dir,self.known_dir)
        self.assertTrue(type(result) is numpy.ndarray )

        method = self.cam1.generate_faceEncode
        self.assertRaises(Exception,method,'0010',self.new_dir,self.known_dir)
    


if __name__ == "__main__":
    unittest.main()