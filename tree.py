"""Python 3.8.1 implementation `ascitree`

to run default example type: python tree.py
to run parse custom tree: python tree.py --str "(String what (should be parsed example))"

"""

import argparse

parser = argparse.ArgumentParser(
    description='Cкрипт, який приймає на вхід текстовий опис дерева і друкує його так, як утиліта asciitre')

parser.add_argument('--str', default='(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))',
                    help="Build tree and show it from string. default example: \
(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))")


class Node:
    def __init__(self, data, child):
        self.value = data
        self.child = child

    def __repr__(self):
        return '{}{}'.format(self.value, ': {}'.format(self.child) if self.child else '')


def print_node(node, depth=0, no_bar=False):
    if depth != 0:
        tab = ' '

        if depth != 1:
            tab += ' ' if no_bar else '|'
            tab += ' ' * 3 + ' ' * 4 * (depth - 2)

        tab += '+-- '
        print('{}{}'.format(tab, node.value))
    else:
        print(node.value)

    if node.child:
        length = len(node.child)
        for i in range(0, length):
            no_bar_decided = (i == length - 1 and depth == 0)
            print_node(node.child[i], depth + 1, no_bar or no_bar_decided)


def build_leaf(string):
    return Node(string, None)


def build_node(string):
    s = string[1:-1]
    elements = []
    seen_open_bracket = 0
    tmp = str()

    if string[0] != '(' or string[-1] != ')':
        return build_leaf(string)

    for el in s:
        if el == ' ' and seen_open_bracket == 0:
            elements.append(tmp) if len(tmp) > 0 else 0
            tmp = str()
            continue

        tmp = tmp + el
        seen_open_bracket += 1 if el == '(' else 0

        if el == ')':
            seen_open_bracket -= 1
            if seen_open_bracket < 0:
                raise NameError("Format error")
            if seen_open_bracket == 0:
                elements.append(tmp)
                tmp = str()
                continue

    elements.append(tmp) if len(tmp) > 0 else 0

    head = elements[0]
    elements = elements[1:]
    if len(elements) == 0:
        return build_leaf(head)

    return Node(head, list(map(build_node, elements)))


def build_tree(input_string):
    if len(input_string) <= 2:
        raise NameError('String too short')
    if input_string[0] != '(' or input_string[-1] != ')':
        raise NameError('Format error')

    return build_node(input_string)


if __name__ == "__main__":
    args = parser.parse_args()
    tree_from_str = build_tree(args.str)
    print_node(tree_from_str)
