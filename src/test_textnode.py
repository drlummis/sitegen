import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node  = TextNode("This is a text node", TextType.BOLD, "www.abc.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.abc.com")
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node  = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("xThis is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node  = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.abc.com")
        self.assertNotEqual(node, node2)

    def test_eq_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        rep = "TextNode(This is a text node, normal, https://www.boot.dev)"
        self.assertEqual(rep, repr(node))
        
if __name__ == "__main__":
    unittest.main()
