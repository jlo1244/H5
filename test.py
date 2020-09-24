import unittest
import Sql

value = "('test', )"


class MyTestCase(unittest.TestCase):
    def testSql(self):
        Sql.insert('test', 'test', 200)
        Sql.cursor.execute('''select uname from test where uname like 'test' ''')
        Sql.cursor.commit
        user = Sql.cursor.fetchone()
        self.assertEqual(user.uname, 'test')
        Sql.cursor.execute('''select id from test where uname like 'test' ''')
        Sql.cursor.commit
        rid = Sql.cursor.fetchone()
        Sql.delete('test', rid.id)
        Sql.cursor.execute('''select uname from test where uname like 'test' ''')
        Sql.cursor.commit
        testing = Sql.cursor.fetchone()
        self.assertIsNone(testing)


if __name__ == '__main__':
    unittest.main()
    MyTestCase.testSql()
