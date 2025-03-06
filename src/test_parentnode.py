import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_parent_to_html_tag_1(self):
        node = ParentNode("p", [ ])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_parent_to_html_tag_2(self):
        node = ParentNode("p", [ ], { "prop" : "value" })
        self.assertEqual(node.to_html(), '<p prop="value"></p>')

    def test_parent_to_html_tag_3(self):
        node = ParentNode("p",
            [ 
                LeafNode(None, "text")
            ]
        )
        self.assertEqual(node.to_html(), "<p>text</p>")

    def test_parent_to_html_tag_4(self):
        node = ParentNode("p",
            [ 
                LeafNode(None, "text"),
                LeafNode("b", "btext")
            ],
            { "prop1" : "value1", "prop2" : "value2" }
        )
        self.assertEqual(node.to_html(), '<p prop1="value1" prop2="value2">text<b>btext</b></p>')

    def test_parent_to_html_tag_5(self):
        node = ParentNode("div",
            [
                ParentNode("p", [])
            ]
        )
        self.assertEqual(node.to_html(), "<div><p></p></div>")

    def test_parent_to_html_tag_6(self):
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
