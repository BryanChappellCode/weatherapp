import unittest
import src.functions as func

class test_functions(unittest.TestCase):

    def test_init_properties(self):

        print("============================================================")
        print("TESTING: init_properties()")
        props = func.init_properties()
        self.assertIsInstance(props, dict)
        print("RESULT: ", props)
        

    


