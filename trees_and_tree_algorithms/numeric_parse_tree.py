from data_structures.stack import Stack
from trees_and_tree_algorithms.binary_tree import BinaryTree

import operator


def build_numeric_parse_tree(numeric_expression):
    trace_stack = Stack()
    tree = BinaryTree(None)
    trace_stack.push(tree)   # the last ) will return the origin tree
    current_tree = tree
    for i in numeric_expression.replace(' ', ''):
        print i
        if i == '(':
            current_tree.insert_left(None)
            trace_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.root = int(i)
            current_tree = trace_stack.pop()
        elif i in ['+', '-', '*', '/']:
            current_tree.root = i
            current_tree.insert_right(None)
            trace_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif i == ')':
            current_tree = trace_stack.pop()

    return current_tree


def evaluate_numeric_parse_tree(tree):
    operators_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_child = tree.left_child
    right_child = tree.right_child

    if left_child and right_child:
        fn = operators_dict[tree.root]
        return fn(evaluate_numeric_parse_tree(left_child), evaluate_numeric_parse_tree(right_child))
    else:
        return tree.root


def post_order_evaluate(numeric_parse_tree):
    operators_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    if isinstance(numeric_parse_tree, BinaryTree):
        left_tree = post_order_evaluate(numeric_parse_tree.left_child)
        right_tree = post_order_evaluate(numeric_parse_tree.right_child)
        if left_tree and right_tree:
            return operators_dict[numeric_parse_tree.root](left_tree, right_tree)
        else:
            return numeric_parse_tree.root


def get_numeric_expression(numeric_parse_tree):

    result = ""
    if isinstance(numeric_parse_tree, BinaryTree):
        # left
        if numeric_parse_tree.left_child:
            result = "(" + get_numeric_expression(numeric_parse_tree.left_child)
        # root
        result += str(numeric_parse_tree.root)
        # right
        if numeric_parse_tree.right_child:
            result += get_numeric_expression(numeric_parse_tree.right_child) + ")"
    return result
