import unittest
import filecmp
import subprocess
from huffman import *


class TestList(unittest.TestCase):
    # def test_cnt_freq(self):
    #     freqlist = cnt_freq("file2.txt")
    #     anslist = [2, 4, 8, 16, 0, 2, 0]
    #     self.assertListEqual(freqlist[97:104], anslist)
    #
    # def test_create_huff_tree(self):
    #     freqlist = cnt_freq("file2.txt")
    #     hufftree = create_huff_tree(freqlist)
    #     self.assertEqual(hufftree.right.freq, 16)
    #     self.assertEqual(hufftree.freq, 32)
    #     self.assertEqual(hufftree.char, 97)
    #     left = hufftree.left
    #     self.assertEqual(left.freq, 16)
    #     self.assertEqual(left.char, 97)
    #     right = hufftree.right
    #     self.assertEqual(right.freq, 16)
    #     self.assertEqual(right.char, 100)
    #
    #
    # def test_create_header(self):
    #     freqlist = cnt_freq("file2.txt")
    #     self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
    #     freqlist = cnt_freq("declaration.txt")
    #     self.assertEqual(create_header(freqlist), "10 166 32 1225 38 1 39 1 44 109 45 3 46 36 49 1 52 1 54 1 55 2 58 10 59 10 65 22 66 7 67 19 68 5 69 3 70 17 71 15 72 24 73 8 74 5 75 1 76 15 77 3 78 8 79 6 80 23 82 9 83 23 84 15 85 3 87 13 97 466 98 88 99 171 100 253 101 875 102 169 103 116 104 331 105 451 106 12 107 13 108 216 109 144 110 487 111 518 112 116 113 6 114 420 115 460 116 640 117 211 118 74 119 84 120 9 121 82 122 4")
    #
    # def test_create_code(self):
    #     freqlist = cnt_freq("file2.txt")
    #     hufftree = create_huff_tree(freqlist)
    #     codes = create_code(hufftree)
    #     self.assertEqual(codes[ord('d')], '1')
    #     self.assertEqual(codes[ord('a')], '0000')
    #     self.assertEqual(codes[ord('f')], '0001')
    #
    # def test_01_singlelinefile(self):
    #     huffman_encode("file1.txt", "file1_out.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call("diff -wb  file1_soln.txt file1_out.txt",
    #                           shell=True)
    #     self.assertEqual(err, 0)

    # def test_02_singlelinefile(self):
    #     huffman_encode("file2.txt", "file2_out.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call("diff -wb  file2_soln.txt file2_out.txt",
    #                           shell=True)
    #     self.assertEqual(err, 0)
    #
    # def test_02_multilinefile(self):
    #     huffman_encode("multiline.txt", "multiline_out.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call("diff -wb  multiline_soln.txt multiline_out.txt",
    #                           shell=True)
    #     self.assertEqual(err, 0)
    #
    def test_edges(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("idontknow", "heey")
    #     huffman_encode("one_character_JV.txt", "one_character_JV_out.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call("diff -wb  one_character_JV_out.txt one_character_JV_solution.txt",
    #                           shell=True)
    #     self.assertEqual(err, 0)
    #     huffman_encode("empty_JV.txt", "empty_JV_out.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call(
    #         "diff -wb  empty_JV_out.txt empty_JV_soln.txt",
    #         shell=True)
    #     self.assertEqual(err, 0)
    #
    # def test_01_declaration(self):
    #     huffman_encode("declaration.txt", "declaration_out.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call("diff -wb  declaration_soln.txt "
    #                           "declaration_out.txt",
    #                           shell=True)
    #     self.assertEqual(err, 0)

    # def test_decode_war_and_peace(self):
    #     huffman_encode("project4_Concordance/War_And_Peace.txt", "War_And_Peace_out.txt")
    #     huffman_decode("War_And_Peace_out.txt", "War_And_Peace_decoded.txt")
    #     # capture errors by running 'diff' on your encoded file with a
    #     # *known* solution file
    #     err = subprocess.call("diff -wb  War_And_Peace.txt "
    #                           "War_And_Peace_decoded.txt",
    #                           shell=True)
    #     self.assertEqual(err, 0)

    def test_decode_declaration(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        huffman_decode("declaration_out.txt", "declaration_decoded.txt")
        # capture errors by running 'diff' on your encoded file with a
        # *known* solution file
        err = subprocess.call("diff -wb  declaration.txt "
                              "declaration_decoded.txt",
                              shell=True)
        self.assertEqual(err, 0)

    def test_decode_1_char(self):
        huffman_encode("one_character_JV.txt", "one_JV")
        huffman_decode("one_JV", "one_decoded_JV.txt")
        # capture errors by running 'diff' on your encoded file with a
        # *known* solution file
        err = subprocess.call("diff -wb  one_decoded_JV.txt "
                              "one_character_JV.txt",
                              shell=True)
        self.assertEqual(err, 0)

    def test_empty(self):
        huffman_encode("empty_JV.txt", "emp_JV.txt")
        huffman_decode("emp_JV.txt", "emp_dec_JV.txt")
        # capture errors by running 'diff' on your encoded file with a
        # *known* solution file
        err = subprocess.call("diff -wb  emp_dec_JV.txt "
                              "empty_JV.txt",
                              shell=True)
        self.assertEqual(err, 0)

    def test_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode("blehajhjaskn.txt", "batman.txt")
        self.assertEqual(parse_header(""), [0] * 256)

if __name__ == '__main__':
    unittest.main()
