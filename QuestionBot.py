#Imported libraries.

import spacy, wikipedia #pip install wikipedia

#Natural language processing in English.

nlp = spacy.load('en')

#Created AskQuestion function.

def AskQuestion():

    #User can input their desired question.

    Question = input("Enter question: ")
    print("\n")

    #Doc saves the natural language processing version of the question.
    doc = nlp(Question)

    #Entities are found, and noun chunks are found in the question.
    entities = doc.ents
    ncs = doc.noun_chunks

    #Saves the noun chunks into a nlp string called TargetSubject.
    for n in ncs:
        TargetSubject = n
        
    #Convert TargetSubject into a string.
    a = str(TargetSubject)

    #Assign QuestionType to an empty list. This is for words like 'who'.
    QuestionType = []
    
    #Iteration over the question to find the word type.
    for word in doc:
        if word.pos_ == 'ADV' and word.dep_ == 'advmod':
            QuestionType.append(word)

        elif word.pos_ == 'NOUN' and word.dep == 'nsubj':
            QuestionType.append(word)

    #Assign QuestionDetails to an empty list. This is for the details in the question.
    QuestionDetails = []
    
    #Iteration over the questino to find details that will help answer the question.
    for word in doc:
        
        if word.pos_ == 'ADJ':
            QuestionDetails.append(word)

        elif word.pos_ == 'VERB' and word.dep_ == 'ROOT':
            QuestionDetails.append(word)

        elif word.pos_ == 'NOUN':
            QuestionDetails.append(word)

    #Splits the target subject into different words.
    SplitWords = a.split()
    
    #Assign URLWords to an empty list.
    URLWords = []
    
    #Iterates over the noun words.
    for item in SplitWords:
        #If not the last item in the list, add a + to the end of the word.
        #This helps to input the URL.
        if item != SplitWords[-1]:
            item = item + "+"
            #Adds the word into the URLWords list.
            URLWords.append(item)

        #If it is the last word, then add it to the list at the end.
        else:
            URLWords.append(item)

    #Empty string ready to add all of the URLWords list items together.        
    StringURLWords = ""

    #Iteration over the URLWords list.
    for item in URLWords:
        #Add each word to the string.
        StringURLWords += item

    #Tries to find the Wikipedia page for the desired question.    
    try:        
        WikiAddress = wikipedia.page(StringURLWords)

    #If it is not found, an apology is said by the program.
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
        print("\nSorry, there seems to be no page linked to your question\n")
        #Lets the user ask another question.
        AskQuestion()

    #The content of the Wikpedia page, or just the text is found.
    WikiContent = WikiAddress.content

    #The NLP version of the content is made.
    NLPWiki = nlp(WikiContent)
    
    #It is now broken down into sentences.
    sentences = NLPWiki.sents

    #String 'x' is created.
    x = ""

    #Iterates over QuestionDetails and adds the whole thing into a string with spaces.
    for i in QuestionDetails:
        x += (str(i) + " ")

    #Created nlp version of x.
    nlpx = nlp(x)

    #Created a token
    token = nlpx[0]

    #Iterates over the sentences to be able to find if a word is in the sentence.
    for sentence in sentences:
        for word in sentence:
            if word == token:
                #If the word is in the question details, print the sentence.
                print(sentence)

    #Since the question is finished, the content is reset.
    NLPWiki = None
    
    #No need to return anything.
    return None

#Main function to call the code to work.

def Main():

    #AskQuestion function is called.
    AskQuestion()

    #Exception handling to only let the user enter yes or no to trying again.
    while True:
        try:
            #Asks the user to input yes or no. Makes input lower case
            Again = input("\nAsk more questions? Yes or No? ").lower()

            #If yes or no, they both break out of the loop.
            if Again == 'yes':
                break

            elif Again == 'no':
                break

        #If yes or no are not entered, they are prompted to enter yes or no.
        except:
            print("\nENTER YES OR NO\n")
            
    #If the user wants to ask another question, they can. Function is called again.
    if Again == 'yes':
        print("\n")
        Main()

    #If they do not want to ask another question, the program exits.
    elif Again == 'no':
        exit()

    #No need to return anything.
    return None

#Main procedure is called.
Main()

