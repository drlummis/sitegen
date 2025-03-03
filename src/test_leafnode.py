import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_tag_1(self):
        node = LeafNode("tag", "Some text")
        self.assertEqual(node.to_html(), "<tag>Some text</tag>")

    def test_leaf_to_html_tag_2(self):
        node = LeafNode("tag", "Some text", {})
        self.assertEqual(node.to_html(), "<tag>Some text</tag>")

    def test_leaf_to_html_tag_3(self):
        node = LeafNode("tag", "Some text", {"prop" : "value"})
        self.assertEqual(node.to_html(), '<tag prop="value">Some text</tag>')

    def test_leaf_to_html_tag_4(self):
        node = LeafNode("tag", "Some text", {"prop1" : "value1", "prop2" : "value2"})
        self.assertEqual(node.to_html(), '<tag prop1="value1" prop2="value2">Some text</tag>')

if __name__ == "__main__":
    unittest.main()
