import unittest
import Sql

value = "('test', )"


class MyTestCase(unittest.TestCase):
    def testSql(self):
        Sql.insert('test', 'test', 200)
        Sql.cursor.execute('''select uname from test where uname like 'test' ''')
        Sql.cursor.commit
        user = Sql.cursor.fetchone()
        self.assertEqual(user.uname, "test")
        Sql.delete('test', 3)
    # should have worked no idea why not


if __name__ == '__main__':
    unittest.main()
    MyTestCase.testSql()
