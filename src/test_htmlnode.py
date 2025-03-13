import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):

    def test_values(self):
        tag = "tag"
        value = "value"
        children = None
        props = {"prop1": "value1", "prop2": "value2"}
        node  = HTMLNode(tag, value, children, props)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_props_to_html_no_props(self):
        node  = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_one_prop(self):
        node  = HTMLNode(None, None, None, {"prop": "value"})
        self.assertEqual(node.props_to_html(), ' prop="value"')

    def test_props_to_html_two_props(self):
        node  = HTMLNode(None, None, None, {"prop1": "value1", "prop2": "value2"})
        self.assertEqual(node.props_to_html(), ' prop1="value1" prop2="value2"')

    def test_repr(self):
        node  = HTMLNode("tag", "value", None, {"prop1": "value1", "prop2": "value2"})
        rep = "HTMLNode(tag, value, children: None, {'prop1': 'value1', 'prop2': 'value2'})"
        self.assertEqual(rep, repr(node))

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "btext")
        self.assertEqual(node.to_html(), "<b>btext</b>")

    def test_leaf_to_html_a_no_props(self):
        node = LeafNode("a", "atext", {})
        self.assertEqual(node.to_html(), "<a>atext</a>")

    def test_leaf_to_html_a_one_prop(self):
        node = LeafNode("a", "atext", {"prop": "value"})
        self.assertEqual(node.to_html(), '<a prop="value">atext</a>')

    def test_leaf_to_html_a_two_props(self):
        node = LeafNode("a", "atext", {"prop1": "value1", "prop2": "value2"})
        self.assertEqual(node.to_html(), '<a prop1="value1" prop2="value2">atext</a>')

    def test_repr(self):
        node  = LeafNode("tag", "value", {"prop1": "value1", "prop2": "value2"})
        self.assertEqual(repr(node), "LeafNode(tag, value, {'prop1': 'value1', 'prop2': 'value2'})")

class TestParentNode(unittest.TestCase):

    def test_parent_to_html_p_no_children_no_props(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_parent_to_html_p_no_children_one_prop(self):
        node = ParentNode("p", [], { "prop" : "value" })
        self.assertEqual(node.to_html(), '<p prop="value"></p>')

    def test_parent_to_html_p_one_child_no_props(self):
        node = ParentNode("p",
            [ 
                LeafNode(None, "text")
            ]
        )
        self.assertEqual(node.to_html(), "<p>text</p>")

    def test_parent_to_html_p_two_children_two_props(self):
        node = ParentNode("p",
            [ 
                LeafNode(None, "text"),
                LeafNode("b", "btext")
            ],
            { "prop1" : "value1", "prop2" : "value2" }
        )
        self.assertEqual(node.to_html(), '<p prop1="value1" prop2="value2">text<b>btext</b></p>')

    def test_parent_to_html_div_one_nested_parent(self):
        node = ParentNode("div",
            [
                ParentNode("p", [])
            ]
        )
        self.assertEqual(node.to_html(), "<div><p></p></div>")

    def test_parent_to_html_div_multiple_nested(self):
        node = ParentNode("div",
            [
                LeafNode("b", "btext"),
                ParentNode("p",
                    [
                        LeafNode(None, "text")
                    ]
                ),
                ParentNode("p",
                    [
                        LeafNode("b", "btext"),
                        LeafNode("i", "itext")
                    ]
                ),
                LeafNode("b", "btext")
            ]
        )
        self.assertEqual(node.to_html(), "<div><b>btext</b><p>text</p><p><b>btext</b><i>itext</i></p><b>btext</b></div>")

if __name__ == "__main__":
    unittest.main()
