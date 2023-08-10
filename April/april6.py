# Reverse words in a given String

def reverse(sentence):

    word = sentence.split(' ')

    reverse_sentence = ' '.join(reversed(word))

    return reverse_sentence

if __name__ == "__main__":
    input = input("Enter sentence :")
    print(reverse(input))