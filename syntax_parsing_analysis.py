from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text of choice here

text = open("dorian_gray.txt",encoding='utf-8').read().lower()

# sentence and word tokenize text here

word_tokenize = word_sentence_tokenize(text)
# print(word_tokenize)

# store and print any word tokenized sentence here

single_word = word_tokenize[100]
# print(single_word)

# create a list to hold part-of-speech tagged sentences here

pos_tagged_text = []

# create a for loop through each word tokenized sentence here

for word in word_tokenize:
  
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(word))

# store and print any part-of-speech tagged sentence here
single_pos = pos_tagged_text[100]
# print(pos_tagged_text)
# print(single_pos)

# define noun phrase chunk grammar here
noun_chunk_grammar = "NP:{<DT><JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(noun_chunk_grammar)

# define verb phrase chunk grammar here
verb_chunk_grammar = "NP:{<DT>?<JJ>*<NN><VB.*><RB.?>?}"


# create verb phrase RegexpParser object here
vp_chuck_parser = RegexpParser(verb_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = []
vp_chunked_text = []

# create a for loop through each pos-tagged sentence here
for word in pos_tagged_text:
  # chunk each sentence and append to lists here
  np_chunked_text.append(np_chunk_parser.parse(word))
  vp_chunked_text.append(vp_chuck_parser.parse(word))
  

# store and print the most common NP-chunks here
# print(np_chunked_text)


# store and print the most common VP-chunks here
# print(vp_chunked_text)

#analyze the chunks
most_common_np = np_chunk_counter(np_chunked_text)
most_common_vp = np_chunk_counter(vp_chunked_text)

print(most_common_np)
print(most_common_vp)
