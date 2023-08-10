# Search engine

def matchingWords(sentence1, sentence2):
    # split the sentences
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.srtrip().split(" ")

    score = 0

    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")

            # convert word1 and word2 into lowercase
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':

    sentences = [
        "This is good",
        "Python is good",
        "This is not a snake",
        "python is easier than java"
    ]

    # input string from user
    qry = input("Plese enter query string : ")

    scores = [matchingWords(qry, sentence) for sentence in sentences]
    # print(scores)

    sortedSentScore = [
        sentScore for sentScore in sorted(zip(scores, sentences) , reverse = True)if sentScore[0] != 0]
    
    # print(sortedSentScore)
    print(f"{len(sortedSentScore)} results found \n")
    
    for score,item in sortedSentScore:
        print(f" \"{item}\" : with the score of {score}\n")