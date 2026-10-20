def split_words(sentence):
        sentence=sentence.lower()
        raw_words=sentence.split()
        cleaned=[]
        for word in raw_words:
            word =word.strip(".,!?;:")
            if word!="":
                cleaned.append(word)
        return cleaned

print(split_words("The Cat Sat on the mat"))
print(split_words("hello world!"))
def build_index(documents):                      # define a function that takes a list of document strings
    index = {}                                   # empty dictionary: word -> list of document IDs
    for doc_id, text in enumerate(documents):    # loop through documents; doc_id is 0, 1, 2... and text is the document
        words = split_words(text)                # turn this document into a clean list of lowercase words
        for word in words:                       # loop through each word in this document
            if word not in index:                # is this word new to the index?
                index[word] = []                 # yes: create an empty list for it
            if doc_id not in index[word]:        # has this document already been recorded for this word?
                index[word].append(doc_id)       # no: add the document ID to the word's list
    return index                                 # after all documents are processed, send back the finished index
docs=["the cat sat","the dog chased the cat"]
print(build_index(docs))
