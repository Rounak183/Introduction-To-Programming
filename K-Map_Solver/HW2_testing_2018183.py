import unittest
from HW2_2018183 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc("w'xz'+wx'y+wz OR w'xz'+wz+x'yz'",minFunc(4,'(4,6,9,10,11,13) d(2,12,15)')))
		self.assertEqual(minFunc("w'y'+wy+x",minFunc(3,'(0,2,5,6) d(3,7)')))
		self.assertEqual(minFunc("w'",minFunc(2,'(0,1) d(3)')))
		self.assertEqual(minFunc("wxyz",minFunc(4,'(0,1,3,4,5,6,8,10,12) d(2,7,9,11,13,14,15)')))
		self.assertEqual(minFunc("w+xy",minFunc(4,'(6,7,8,9) d(10,11,12,13,14,15)')))
		self.assertEqual(minFunc("x'y'+yz",minFunc(4,'(0,1,3,7,8,9,11,15)')))
                
if __name__=='__main__':
	unittest.main()
