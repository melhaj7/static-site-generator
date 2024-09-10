from htmlnode import HTMLNode


def main():
    node = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
    }
    )

    node.props_to_html()


if __name__ == "__main__":
    main()
