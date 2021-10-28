"""
Python Problem 7: Solution | Python Tutorials For Absolute Beginners In Hindi #116
This is the solution to Python Problem # 7. You can see the problem statement below:-

Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

auther gauresh
perpose: practice problem

Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
"""
def matchingword(sentence1,sentence2):
    words1=sentence1.strip().split()
    words2=sentence2.strip().split()
    score=0
    for word1 in words1:
        for word2 in words2:
            #print(f"matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return  score
if __name__ == "__main__":
    #print( matchingword("Python is cool", "python is good"))
       Sentences = ["Python is cool", "python is good", "python is not  snake"]
       query = input("Enter query string\n")
       score = [matchingword(query,sentence) for sentence in Sentences]
       #print(score)
       sortedscore=[sentscore for sentscore in sorted(zip(score,Sentences), reverse = True) ]
       #print(sortedscore)

       print(f"{len(sortedscore)} result found")
       for score ,item in sortedscore:
           print(f"{item} {score}")