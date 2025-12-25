class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find('#', i)

            length = int(s[i:delimiter_pos])

            i = delimiter_pos + 1 #one position ahead of delim

            actual_string = s[i:i + length]
            result.append(actual_string)

            i += length

        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

'''
Design -
Encode : convert a list of strings to a single string
Decode : convert string back to original form (decode it)
i/p : [" "," "," "]
encode() : [".........."]
decode() : [" "," "," "]

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Encode Strategy : take in the i/p + delimiter
    "length of string + dummy delimiter(#) + string"
    "5#Hello5#World"
Decode Strategy : read the encoded i/p
    "Read the length + skip our delimiter(#) = exact no. of chars in each ""list""

Step 1 (encoding):
    i/p: ["Hello","World"]
    "Hello" -> len(5) -> "5#Hello"
    "World" -> len(5) -> "5#World"
    Encoded String : "5#Hello5#World"
Step 2 (decoding):
    i/p : ["5#Hello5#World"]
    i = 0 : we find '5', we find '#', extract "Hello"
    i = 7 : we find '5', we find '#', extract "World"
    Output: ["Hello","World"]
'''
