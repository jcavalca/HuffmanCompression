class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code
        # value
        self.freq = freq  # the frequency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __gt__(self, other):
        if self.freq == other.freq:
            return self.char > other.char
        return self.freq > other.freq

    def helper_code(self, node, help_list, code):
        if node.left is None and node.right is None:
            help_list.append([node.char, code])
        if node.left is not None:
            self.helper_code(node.left, help_list, code + "0")
        if node.right is not None:
            self.helper_code(node.right, help_list, code + "1")
        return help_list

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the
    "lesser node" on the left The new node's frequency value will be the sum
    of the a and b frequencies The new node's char value will be the lesser
    of the a and b char ASCII values """
    new_freq = a.freq + b.freq
    if a.freq < b.freq and a.freq != b.freq:
        new_node = HuffmanNode(b.char, new_freq)
    if b.char > a.char:
        new_node = HuffmanNode(a.char, new_freq)
    new_node.set_left(a)
    new_node.set_right(b)
    return new_node


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and
    counts the frequency of occurrences of all the characters within that
    file """
    char_freq = [0] * 256
    file = open(filename)
    for i in file.readlines():
        for j in i:
            char_freq[ord(j)] += 1
    file.close()
    return char_freq


def create_huff_tree(cnt_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    node_list = []
    count = 0
    for i in cnt_freq:
        if i != 0:
            node_list.append(HuffmanNode(count, i))
        count += 1
    while len(node_list) > 1:
        node_list.sort()
        node_list[0] = combine(node_list[0], node_list[1])
        node_list.pop(1)
    huffman_tree = node_list[0]
    return huffman_tree


def create_code(root_node):
    """Returns an array (Python list) of Huffman codes. For each character,
    use the integer ASCII representation as the index into the array,
    with the resulting Huffman code for that character stored at that
    location """
    code_list = [""] * 256
    helper_list = root_node.helper_code(root_node, [], "")
    for i in helper_list:
        code_list[i[0]] = i[1]
    return code_list


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the
    output file Example: For the frequency list associated with "aaabbbbcc,
    would return “97 3 98 4 99 2” """
    output = ""
    count = 0
    for j in freqs:
        if j != 0:
            if output == "":
                output += str(count) + " " + str(j)
            else:
                output += " " + str(count) + " " + str(j)
        count += 1
    return output


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters Uses the
    Huffman coding process on the text from the input file and writes encoded
    text to output file Take not of special cases - empty file and file with
    only one unique character """
    try:
        file = open(in_file)
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError
    count_freq = cnt_freq(in_file)
    header = create_header(count_freq)
    if len(header) == 0:
        output_file = open(out_file, "w", newline="")
        output_file.close()
        return
    output_file = open(out_file, "w", newline="")
    output_file.write(header)
    huffman_tree = create_huff_tree(count_freq)
    code_list = create_code(huffman_tree)
    file = open(in_file)
    out_string = ""
    letters_to_be_encoded = file.readlines()
    for i in letters_to_be_encoded:
        for j in i:
            out_string += code_list[ord(j)]
    if out_string != "":
        output_file.write("\n" + out_string)
    file.close()
    output_file.close()


def parse_header(header_string):
    header_string = header_string.split()
    if not header_string:
        return [0] * 256
    else:
        # header_string_list = header_string.split()
        freq_list = [0] * 256
        while len(header_string) > 1:
            freq_list[int(header_string[0])] = int(header_string[1])
            header_string.pop(0)
            header_string.pop(0)
        return freq_list


def helper_decode(huffman_tree, encoded_string, decode_file):
    count = 0
    output_file = open(decode_file, "w", newline="")
    node = huffman_tree
    while count < len(encoded_string):
        if node.right is None and node.left is None:
            output_file.write(chr(node.char))
            node = huffman_tree
        elif encoded_string[count] == "1":
            node = node.right
            count += 1
        elif encoded_string[count] == "0":
            node = node.left
            count += 1
    output_file.write(chr(node.char))
    output_file.close()


def huffman_decode(encoded_file, decoded_file):
    try:
        file = open(encoded_file)
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError
    enc_file = open(encoded_file)
    lines = enc_file.readlines()
    if not lines:
        output_file = open(decoded_file, "w", newline="")
        output_file.write("")
        output_file.close()
        enc_file.close()
        return
    else:
        first_line_list = lines[0].split()
        try:
            second_line = lines[1]
            freq_list = parse_header(lines[0])
            huffman_tree = create_huff_tree(freq_list)
            helper_decode(huffman_tree, second_line, decoded_file)
            enc_file.close()
        except IndexError:
            # first_line_list = lines[0].split()
            output_file = open(decoded_file, "w", newline="")
            for i in range(int(first_line_list[1])):
                output_file.write(chr(int(first_line_list[0])))
            output_file.close()
            enc_file.close()

huffman_encode("shoeless.txt", "sol.txt")