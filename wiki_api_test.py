import unittest
from wiki_api import get_random_wiki, get_wiki, get_keywords

class WikiTest(unittest.TestCase):
    def assertValidArticleFormat(self, data):
        self.assertTrue("text" in data, "Missing field: ['text']")
        self.assertTrue("id" in data, "Missing field ['id']")
        self.assertTrue("keywords" in data, "Missing field ['keywords']")

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

class TestKeywords(WikiTest):
    def test_get_keywords(self):
        res = get_keywords('"Hello,_World!"_program')
        self.assertIsNotNone(res, "Empty response")
        self.assertIsInstance(res, list)
        self.assertEqual(len(list(set(res))), len(res))

if __name__ == '__main__':
    unittest.main()