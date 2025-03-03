class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Render the node as HTML.
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        # Returns a string that represents the HTML attributes of the node.
        if self.props == None:
            return ""
        html = ""
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html

    def __eq__(self, textnode):
        return self.tag == textnode.tag and \
               self.value == textnode.value and \
               self.children == textnode.children and \
               self.props == textnode.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
