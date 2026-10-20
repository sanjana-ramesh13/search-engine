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
print(split_words("!"))
def  build_index(documents):
     index={}
     for doc_id, text in enumerate(documents):
          words=split_words(text)
          for word in words:
               if word not in index:
                    index[word]=[]
               if doc_id not in index[word]:
                    index[word].append(doc_id)
          return index
docs=["the cat sat","the dog chased the cat"]
print(build_index(docs))
