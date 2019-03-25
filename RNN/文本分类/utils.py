import pickle
import os
import numpy as np
import nltk

from tqdm import tqdm

class Project:
    def __init__(self, root_dir):
        self._root_dir = root_dir
        self._init_all_path()

    def _init_all_path(self):
        self._data_dir = os.path.join(self._root_dir, 'data')
        self._auxx_data_dir = os.path.join(self._data_dir, 'auxx')
        self._neg_train_data_dir = os.path.join(self._data_dir,'aclImdb/train/neg')
        self._pos_train_data_dir = os.path.join(self._data_dir,'aclImdb/train/pos')
        self._neg_test_data_dir = os.path.join(self._data_dir,'aclImdb/test/neg')
        self._pos_test_data_dir = os.path.join(self._data_dir,'aclImdb/test/pos')

    @property
    def neg_train_data_dir(self):
        return self._neg_train_data_dir + os.path.sep

    @property
    def pos_train_data_dir(self):
        return self._pos_train_data_dir + os.path.sep

    @property
    def neg_test_data_dir(self):
        return self._neg_train_data_dir + os.path.sep

    @property
    def pos_test_data_dir(self):
        return self._pos_test_data_dir + os.path.sep

    @staticmethod
    def init(root_dir, create = True):
        project = Project(root_dir)
        if create:
            paths = [
                project._data_dir,
                project._auxx_data_dir
            ]

            for path in paths:
                if os.path.exists(path):
                    continue
                else:
                    os.mkdir(path)

    def get_filenames(self, path):
        for root, dirs, files in os.walk(path):
            print(root)
            print(dirs)
            print(files)
        return files

    def sentence_to_one_file(self):
        print('sentence_to_one_file start ......')
        # neg_file_train = self.get_filenames(self.neg_train_data_dir)
        pos_file_train = self.get_filenames(self.pos_train_data_dir)
        neg_file_test = self.get_filenames(self.neg_test_data_dir)
        pos_file_test = self.get_filenames(self.pos_test_data_dir)

        # self.files_to_one_file(self.pos_train_data_dir, neg_file_train, os.path.join(self._data_dir, 'neg_train.txt'))
        self.files_to_one_file(self.pos_train_data_dir, pos_file_train, os.path.join(self._data_dir, 'pos_train.txt'))
        self.files_to_one_file(self.neg_test_data_dir, neg_file_test, os.path.join(self._data_dir, 'neg_test.txt'))
        self.files_to_one_file(self.pos_test_data_dir, pos_file_test, os.path.join(self._data_dir, 'pos_test.txt'))

        print('sentence_to_one_file finish .....')



    def files_to_one_file(self,basepath,  filenames, target_filename):
        sentences = []
        for filename in tqdm(filenames):
            with open(os.path.join(basepath, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                sentences.append(text)
        text = ''
        for sentence in tqdm(sentences):
            text = text + sentence +'\n'
        with open(target_filename, 'w', encoding='utf-8') as f:
            f.write(text)
        pass


    def word_to_id(self):
        neg_file = self.get_file_word(self.neg_train_data_dir)
        # pos_file = self.get_file_word(self.pos_train_data_dir)
        word_list = []

        for file_name in tqdm(neg_file):
            with open(os.path.join(self.neg_train_data_dir, file_name), 'r', encoding='utf-8') as f:
                text = f.read()
                words = text.split(' ')
                for word in words:
                    if word not in word_list:
                        word_list.append(word)
        print(word_list)
        with open(os.path.join(self._data_dir, 'pos_train_word.txt'), 'w', encoding='utf-8') as file:
            # f.write(word +'\n' for word in word_list)
            text = ''
            for word in word_list:
                text = text + word + '\n'
            file.write(text)



if __name__ == '__main__':
    path = os.getcwd()
    Project.init(path)
    project = Project(path)
    project.sentence_to_one_file()
    # project.word_to_id()
    # word_list = ['hello', 'hi', 'ok']
    # np.savetxt('data/pos_train_word1.txt', word_list)
    # with open('data/pos_train_word.txt1','w', encoding='utf-8') as file:
    #     file.write(str(word_list))
    #     text = ''
    #     for word in word_list:
    #         text = text + word + '\n'
    #     file.write(text)
        # file.write(word for word in word_list)
# def w2v_():
