from . import utils,document

def write(pretext,project_path):
    title = pretext.xpath("/pretext/book/title")[0].text
    utils.ensure_directory(project_path)
    with utils.working_directory(project_path):
        utils.ensure_directory("source")
        pretext.write(
            "source/main.ptx",
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8"
        )
        document.publisher().write(
            "publisher.ptx",
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8"
        )
        with open(".gitignore", mode='w') as gitignore:
            print("output", file=gitignore)
        with open("README.md", mode='w') as readme:
            print(f"# {title}", file=readme)
            print("", file=readme)
            print("Authored with [PreTeXt](https://pretextbook.org).", file=readme)
