from textnode import TextNode, TextType


def main():
    # Create a sample link TextNode
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
