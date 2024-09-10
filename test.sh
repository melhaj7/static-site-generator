# python3 -m unittest discover -s src

#!/bin/bash
# Run only a specific test file
python3 -m unittest src.test_htmlnode

# To run just one test class:
# python3 -m unittest src.test_htmlnode.TestHTMLNode

# To run just one test method:
# python3 -m unittest src.test_htmlnode.TestHTMLNode.test_props_to_html_with_props
