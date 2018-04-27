import io
import re
import pathlib

root = pathlib.Path(__file__).parent

import_regex = re.compile(r'^@import\s+"([\w-]+[.]sass)"\s*$')


def extract_import(line):
    found = import_regex.search(line)
    if not found:
        return

    return found.group(1)


def extract_bulma_sass_imports(padding):
    bulma_sass_path = root.joinpath('../node_modules/bulma/sass')
    targets = bulma_sass_path.glob('**/_all.sass')
    for sass in targets:
        parent_path = str(sass.parent.relative_to(bulma_sass_path)).capitalize()
        yield f'\n{padding}// {parent_path}'
        for src in filter(bool, map(extract_import, sass.open('r').readlines())):
            # relative_path = str(src).replace(str(bulma_sass_path), '')
            # yield f'{padding}@import "bulma/sass/{relative_path}";'
            import_path = sass.parent.joinpath(src)
            sass_lines = io.open(import_path, 'r').readlines()
            yield "\n".join((f'{padding}{line}' for line in sass_lines))


def generate_bulma_imports(padding=4):
    content = "\n".join(extract_bulma_sass_imports(padding))
    return f'.bulma\n{padding}{content}\n'.strip()


def write_file(data):
    path = root.joinpath('sphinx-bulma.src.sass')
    with path.open('w') as stream:
        stream.write(data)

    relative_path = path.relative_to(root)
    print(f'wrote {relative_path}')


def main():
    padding = ' ' * 4
    sass = generate_bulma_imports(padding)
    write_file(sass)


if __name__ == '__main__':
    pass#main()
