from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        # Render the node as HTML.
        if self.tag == None:
            raise ValueError("ParentNode does not have a tag")
        if self.children == None:
            raise ValueError("ParentNode does not have any children")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html

"""
Add a .to_html method.
If the object doesn't have a tag, raise a ValueError.
If children is a missing value, raise a ValueError with a different message.
Otherwise, return a string representing the HTML tag of the node and its children. 
This should be a recursive method (each recursion being called on a nested child node). 
I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.
"""