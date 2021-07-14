import unittest
from wiki_api import get_random_wiki, get_wiki

class WikiTest(unittest.TestCase):
    def assertValidArticleFormat(self, data):
        self.assertTrue("text" in data, "Missing field: ['text']")
        self.assertTrue("id" in data, "Missing field ['id']")

class TestGetRandom(WikiTest):
    def test_random(self):
        res = get_random_wiki()
        self.assertIsNotNone(res, "Empty response")
        self.assertValidArticleFormat(res)

class TestGet(WikiTest):
    def test_get(self):
        res = get_wiki('"Hello,_World!"_program')
        self.assertIsNotNone(res, "Empty response")
        self.assertValidArticleFormat(res)

if __name__ == '__main__':
    unittest.main()