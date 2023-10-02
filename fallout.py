import sys

print("enter the words: ")
inputs = input()
words = inputs.split()

def overlap(check, word):
    count = 0
    for i, c in enumerate(word):
        if check[i] == c:
            count += 1
    return count

try:
    while len(words) > 1:
        print("Enter guess and likeliness: ")
        guess = input()
        arr = guess.split()

        guessed_word = arr[0]
        overlap_count = int(arr[1])
        new_arr = []

        for w in words:
            if w == guessed_word:
                continue

            likeliness = overlap(w, guessed_word)
            if likeliness == overlap_count:
                new_arr.append(w)

        words = new_arr
        print(words)
except:
    sys.exit(0)