import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        tag = "tag"
        value = "value"
        children = [ TextNode("text1", TextType.NORMAL), TextNode("text2", TextType.BOLD) ]
        props = {"prop1" : "value1", "prop2" : "value2"}
        # node  = HTMLNode(tag, value, children, props)
        node  = HTMLNode(tag, value, children, props)
        node2 = HTMLNode(tag, value, children, props)
        self.assertEqual(node, node2)

    def test_values(self):
        tag = "tag"
        value = "value"
        children = [ TextNode("text1", TextType.NORMAL), TextNode("text2", TextType.BOLD) ]
        props = {"prop1" : "value1", "prop2" : "value2"}
        node  = HTMLNode(tag, value, children, props)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_props_to_html_0(self):
        node  = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_1(self):
        props = {"prop" : "value"}
        node  = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(), ' prop="value"')

    def test_props_to_html_2(self):
        props = {"prop1" : "value1", "prop2" : "value2"}
        node  = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(), ' prop1="value1" prop2="value2"')

    def test_repr(self):
        tag = "tag"
        value = "value"
        children = [ TextNode("text1", TextType.NORMAL), TextNode("text2", TextType.BOLD) ]
        props = {"prop1" : "value1", "prop2" : "value2"}
        node  = HTMLNode(tag, value, children, props)
        rep = "HTMLNode(tag, value, children: [TextNode(text1, normal, None), TextNode(text2, bold, None)], {'prop1': 'value1', 'prop2': 'value2'})"
        self.assertEqual(rep, repr(node))

if __name__ == "__main__":
    unittest.main()
