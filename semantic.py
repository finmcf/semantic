# import spacy module

import spacy

# load spacy with 'en_core_web_md' and define as nlp

nlp = spacy.load('en_core_web_md')

# initialize word variables holding each word by calling nlp on each

word1 = nlp("cat")

word2 = nlp("monkey")

word3 = nlp("banana")


# print the similarity between each word using the similarity(method)

print(word1.similarity(word2))

print(word3.similarity(word2))

print(word3.similarity(word1))


# initialize word variables holding each word by calling nlp on each

word4 = nlp("mouse")

word5 = nlp("dog")

word6 = nlp("cheese")


print(word4.similarity(word5))

print(word6.similarity(word5))

print(word6.similarity(word4))


# load spacy with 'en_core_web_sm' and define as nlp


nlp = spacy.load('en_core_web_sm')


# initialize word variables holding each word by calling nlp on each


word1 = nlp("cat")

word2 = nlp("monkey")

word3 = nlp("banana")

# print the similarity between each word using the similarity(method)b

print(word1.similarity(word2))

print(word3.similarity(word2))

print(word3.similarity(word1))

# cat and monkey had the greatest similarity which I expected as they are both animals,
# monkey and banana had a greater similarity than cat and banana, as monkeys eat bananas
# while cats do not, which ins interesting as it considers the relationship between different
# words from different categories.

# I also defined word4, word5 and word6 as mouse, monkey, and cheese, the highest similarity was found between
# mouse and dog which I expected as they are both animals, but I was also expecting there to be a higher similarity
# between mouse and cheese than dog and cheese, as mice are known for eating cheese but this was not the case
# as there was only a marginal difference in similarity which suprised me.

# when using 'en_core_web_sm', the similarities between each words is given but so is the following message:

# UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity
# method will be based on the tagger, parser and NER, which may not give useful similarity judgements.
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with
# word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use
# one of the larger models instead if available.

# So perhaps 'en_core_web_sm' does not load any word vectors to spacy and therefore, spacy cannot work out similarity as
# a well as before with a smaller model, as with 'en_core_web_md', and the similarity calculated between each word seems
# to be similar between all three, unlike with 'en_core_web_md' where there was a much clearer difference
