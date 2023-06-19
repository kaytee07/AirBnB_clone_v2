import unittest
import MySQLdb


class TestStateCreation(unittest.TestCase):
    def setUp(self):
        db = MySQLdb.connect(host='localhost',
                             user='root',
                             passwd='passwordPASS**1234',
                             db='test_db')
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        self.cursor.execute('SELECT COUNT(*) FROM TABLES')
        initial_count = self.cursor.fetchone()[0]

        self.cursor.execute('SELECT COUNT(*) FROM states')
        updated_count = self.cursor.fetchone()[0]

        self.assertEqual(updated_count - initial_count, 1)

if __name__ == '__main__':
    unittest.main()
