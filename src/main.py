from leafnode import LeafNode


def main():
    leaf = LeafNode(
        value="Click here",
        tag="a",
        props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
    leaf2 = LeafNode(
        value="This is a paragraph",
        tag="p",
    )
    leaf3 = LeafNode(value="This is a paragraph")

    print(leaf.to_html())
    print(leaf2.to_html())
    print(leaf3.to_html())


if __name__ == "__main__":
    main()
