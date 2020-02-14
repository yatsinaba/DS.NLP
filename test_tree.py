from unittest import TestCase

class Test(TestCase):
    def test_tree(self):

        expected_output = \
            """asciitree
             +-- sometimes
             |   +-- you
             +-- just
             |   +-- want
             |       +-- to
             |       +-- draw
             +-- trees
             +-- in
                 +-- your
                     +-- terminal"""

        text = "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"
        from tree import Tree
        example_tree, list = Tree.fromString(text)
        example_tree.show()

        assert example_tree.show() == expected_output