from __future__ import absolute_import
import unittest
from lib.flyingcow import register_connection
from tornado.options import options
import string
import random
from six.moves import range

class BaseTestCase(unittest.TestCase):        
    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.db = self.create_database('mltshp_testing')

    def tearDown(self):
        super(BaseTestCase, self).tearDown()

    def create_database(self, name):
        db = register_connection(options.database_host, name, options.database_user, options.database_password)
        db.execute("DROP database IF EXISTS %s" % (name))
        db.execute("CREATE database %s" % (name))
        db.execute("USE %s" % (name))
        f = open("setup/db-install.sql")
        load_query = f.read()
        f.close()
        db.execute(load_query)
        return db
        
    def generate_string_of_len(self, length):
        return ''.join(random.choice(string.letters) for i in range(length))
    
