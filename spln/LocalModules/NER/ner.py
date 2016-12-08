import nltk
import sys
import json

class Verif:
    x = 0

def get_ner(sample):

    if Verif.x == 0:
        nltk.download('all-corpora')
        Verif.x = 1


    def extract_entity_names(t):
        entity_names = []

        if hasattr(t, 'label') and t.label:
            if t.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))

        return entity_names

    sentences = nltk.sent_tokenize(sample)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    entity_names = []
    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)

        entity_names.extend(extract_entity_names(tree))

    # Print all entity names
    #print entity_names

    # Print unique entity names
    data = {}
    data['status'] = 'OK'
    data['message'] = 'Entities found.'
    data['data'] = entity_names
    return data
