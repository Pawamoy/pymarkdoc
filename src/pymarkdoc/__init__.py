import sys
from os.path import abspath, basename, dirname

from getdoc import get_module_doc


__version__ = "0.2.0"


def _get_doc(path):
    try:
        top_dir = __import__(basename(path))
    except ImportError:
        print('pymarkdoc: import error %s' % basename(path))
        return None
    if not hasattr(top_dir, '__file__'):
        print('pymarkdoc: %s is not a package/module' % path)
        return None
    else:
        return get_module_doc(top_dir)


def _doc_to_markdown(d, complete=False, current_module=None, current_class=None):
    lines = []
    if d['type'] == 'module':
        current_module = d['name']
        lines.append('## [`%s`]()' % d['name'])
    elif d['type'] == 'class':
        current_class = d['name']
        line = '**%s**' % d['name']
        if current_module and complete:
            line = '`%s` ' % current_module + line
        lines.append('### [%s]()' % line)
    elif d['type'] == 'function':
        line = '*%s*' % d['name']
        if current_class and complete:
            line = '**%s** ' % current_class + line
        if current_module and complete:
            line = '`%s` ' % current_module + line
        lines.append('#### [%s]()' % line)
    lines.append('')
    if d['doc']:
        lines.append(d['doc'])
        lines.append('')

    if d.get('nest', None) is not None:
        for _d in d['nest']:
            lines.extend(_doc_to_markdown(_d, complete, current_module, current_class))
    return lines


def _module_to_markdown(module, exclude_module=None, exclude_class=None, exclude_function=None, complete=False):
    doc = get_module_doc(module, exclude_module, exclude_class, exclude_function)
    return '\n'.join(_doc_to_markdown(doc, complete))


def write_to_file(file, contents):
    with open(file, 'w') as f:
        f.write(contents)


def main(names):
    paths = list(names)
    if len(paths) == 0:
        paths.append('.')

    for path in paths:
        absolute_path = abspath(path)
        sys.path.append(dirname(absolute_path))
        sys.path.append(absolute_path)

        doc = _get_doc(absolute_path)
        if doc is not None:
            for d in doc:
                print(d)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
