from gensim.models import word2vec
from gensim.models import KeyedVectors
auxx_dir = 'data/auxx/'

def pre_train_w2v(binary = False):

    filenames = [
        'neg_test.txt',
        'neg_train.txt',
        'pos_test.txt',
        'pos_train.txt'
    ]
    texts = []
    for filename in filenames:
        with open('data/' + filename, 'r', encoding='utf-8') as file:
            # while file
            for line in file.readlines():
                texts.append(line.strip().split(" "))
    print(texts[0])
    model = word2vec.Word2Vec(sentences=texts, size=300, window=2, min_count=3, workers=2)
    model.wv.save_word2vec_format(auxx_dir + "train_all_data.bigram", binary=binary, fvocab=None)
    model.save(auxx_dir + 'train_all_data.model')
    print('----finish------')
    pass


if __name__ == '__main__':
    # pre_train_w2v()
    model = word2vec.Word2Vec.load(auxx_dir + "train_all_data.model")
    print(model['of'])
    model2 = KeyedVectors.load_word2vec_format(auxx_dir + "train_all_data.bigram", binary=False)
    print("--------")
    print(model2['of'])
    pass