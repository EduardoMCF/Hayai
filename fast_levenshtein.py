class TrieNode:
    def __init__(self, end: str = None):
        self.children = dict()
        self.end = end

    def __setitem__(self, key, val):
        self.children[key] = val

    def __getitem__(self, key):
        return self.children.get(key, None)


class LevenshTrie:
    def __init__(self, words: list):
        self.root = TrieNode()

        for word in words:
            self.insert(word)

    def insert(self, word: list):
        aux = self.root
        for char in word:
            if aux[char] is None:
                aux[char] = TrieNode()

            aux = aux[char]

        aux.end = word

    def search(self, word: str, maxDist: int):
        ans = []
        stack = [(child, letter, list(range(len(word) + 1)))
                 for letter, child in self.root.children.items()]

        while stack:
            node, letter, parent_row = stack.pop()

            result_row = self._levenshtein(parent_row, letter, word)
            current_dist = result_row[-1]

            if current_dist <= maxDist and node.end is not None:
                ans.append((node.end, current_dist))

            if min(result_row) <= maxDist:
                for letter, child in node.children.items():
                    stack.append((child,
                                  letter,
                                  result_row
                                  ))

        return ans

    def _levenshtein(self, row, letter, word):
        result_row = [row[0] + 1]
        for col in range(1, len(row)):
            result_row.append(min(
                row[col] + 1,
                result_row[-1] + 1,
                row[col-1] + (0 if word[col-1] == letter else 1)
            ))

        return result_row
