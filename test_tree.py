from unittest import TestCase


class Test(TestCase):
    def test_tree(self):
        expected_output = """asciitree
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
        from tree import build_tree, print_node
        import io
        from contextlib import redirect_stdout

        bulded_tree = build_tree('(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))')
        f = io.StringIO()
        with redirect_stdout(f):
            print_node(bulded_tree)

        output = f.getvalue()

        assert output == (expected_output + '\n')
