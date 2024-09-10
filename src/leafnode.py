from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, children=None, props=None):
        super().__init__(tag, value, children, props)

        # if self.children is not None:
        #     raise ValueError("Children are not allowed")

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.tag == "a":
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
