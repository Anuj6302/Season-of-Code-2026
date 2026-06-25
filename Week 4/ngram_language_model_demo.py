# Simple N-gram Language Model Demo

sentence = "ai helps in industrial quality assurance"

words = sentence.split()

ngrams = []

for i in range(len(words)-1):
    pair = (words[i], words[i+1])
    ngrams.append(pair)


print("Generated word pairs:")

for item in ngrams:
    print(item)
