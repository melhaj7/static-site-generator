from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("A parent node must have a tag")
        if self.children is None:
            raise ValueError("A parent node must have children")
        combined_child_tags = ''
        for child in self.children:
            combined_child_tags += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{combined_child_tags}</{self.tag}>"
