# Read lines from a file and convert them into a single sentence with split words
def tokenize(openfile):
    sentence = []
    for line in openfile:
        sentence.extend(line.split())
    return sentence

with open('input.txt', 'r') as f:
    print(tokenize(f))
