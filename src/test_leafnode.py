import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_initialization_no_children(self):
        node = LeafNode(value="test", tag="p")
        self.assertEqual(node.value, "test")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.props, {})
        self.assertIsNone(node.children)

    def test_initialization_with_children(self):
        with self.assertRaises(ValueError) as context:
            LeafNode(value="test", tag="p", children=['child'])
        self.assertEqual(str(context.exception), "Children are not allowed")

    def test_to_html_no_value(self):
        node = LeafNode(value=None, tag="p")
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),
                         "All leaf nodes must have a value")

    def test_to_html_no_tag(self):
        node = LeafNode(value="This is a value")
        self.assertEqual(node.value, "This is a value")

    def test_to_html_tag_is_a(self):
        node = LeafNode(value="Click here", tag="a", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com" target="_blank">Click here</a>')

    def test_to_html_with_tag_not_a(self):
        node = LeafNode(value="This is a paragraph", tag="p")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")


if __name__ == "__main__":
    unittest.main()
