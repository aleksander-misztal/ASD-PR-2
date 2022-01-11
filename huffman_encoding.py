import heapq
from collections import defaultdict


class Output:
    def __init__(self, tab, encoded):
        self.tab = tab
        self.encoded = encoded
        self.pre_size, self.post_size = self.countSizes()

    def countSizes(self):
        f1 = open("files/base_file.txt", "r").read()
        before_compression = len(f1.encode('utf-8')) * 8
        after_compression = len(self.encoded)
        return str(before_compression), str(after_compression)

    def preparedOutput(self):
        result = ""
        result += self.tab + '\n\n' + self.encoded + '\n\n' + "Before compression (in bits) : " + self.pre_size + '\n' + "After compression (in bits) : " + self.post_size
        return result

    def writeToFile(self):
        f = open("files/compressed_text.txt", "w")
        f.write(self.preparedOutput())
        f.close()


def createDict(data):
    count = dict()
    for word in data:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def encode(freq):
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    # Tworze kopiec
    heapq.heapify(heap)
    # Operacje na kopcu
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for value in left[1:]:
            value[1] = '0' + value[1]
        for value in right[1:]:
            value[1] = '1' + value[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def listToDict(data):
    d = dict()
    for element in data:
        if element[0] not in d:
            d[element[0]] = element[1]
    return d


def encodeFile(h, text):
    pattern = listToDict(h)
    result = ""
    for word in text:
        result += str(pattern[word])
    return result


def prepareTab(freq, huffman):
    tab = ""
    tab += str("CHAR".ljust(10) + "TIMES".ljust(10) + "Code") + '\n'
    for i in huffman:
        tab += str(i[0].ljust(10) + str(freq[i[0]]).ljust(10) + i[1]) + '\n'
    return tab


file_txt = open("files/base_file.txt", "r").read()
frequency = createDict(file_txt)
huff = encode(frequency)
# print(huff)
# print(tab)

Output(prepareTab(frequency, huff), encodeFile(huff, file_txt)).writeToFile()
