import unittest

SERVER = "server_b"

class AllAssertsTests(unittest.TestCase):
    
    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("Hola", "Hola")
        
    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("No soy un numero")
            
    def test_assert_in(self):
        self.assertIn(10, [2,3,4,10])
        self.assertNotIn(5, [3,4,2,6])
        
    def test_assert_dicts(self):
        user = {"fist_name": "Luis","last_name": "Martinez"}
        self.assertDictEqual(
            {"fist_name": "Luis","last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1,2,3,4,5},
            {1,2,3,4,5}
        )
    
    @unittest.skip("Trabajo en progreso, sera habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("Hola", "Chao")
        
    @unittest.skipIf(SERVER != "server_a", "Saltada porque no estamos en el servidor")    
    def test_skipIf(self):
        self.assertEqual(1000, 1000)
    
    @unittest.expectedFailure
    def test_expectedfailure(self):
        self.assertEqual(10,100)