import unittest

from env import run_migrations_offline, run_migrations_online

class Test_migration_offline(unittest.TestCase) :

    def Test_migration_online(self) :
        self.assertEqual(run_migrations_offline(), 1)
    
    def Test_migration_already_offline(self) :
        self.assertEqual(run_migrations_offline(), 0)
    
    def Test_migration_offline(self) :
        self.assertEqual(run_migrations_online(), 1)
    
    def Test_migration_already_online(self) :
        self.assertEqual(run_migrations_online(), 0)

if __name__ == '__main__' :
    unittest.main()  