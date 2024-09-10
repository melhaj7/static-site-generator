import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        }
        )
        expected_output = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(props={})
        expected_output = ''
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_no_props(self):
        node = HTMLNode()
        expected_output = ''
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_special_characters(self):
        # Test props with special characters
        node = HTMLNode(props={"data-id": "123&456", "class": 'btn "primary"'})
        expected_output = 'data-id="123&456" class="btn \\"primary\\""'
        self.assertEqual(node.props_to_html(), expected_output)


if __name__ == "__main__":
    unittest.main()
