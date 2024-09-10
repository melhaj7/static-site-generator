class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("Subclasses must implement this method")

    def props_to_html(self):
        def escape_double_quotes(value):
            return value.replace('"', '\\"')

        return " ".join(f'{key}="{escape_double_quotes(value)}"' for key, value in self.props.items())

    def __iter__(self):
        # Allow iteration over the items in props
        return iter(self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
