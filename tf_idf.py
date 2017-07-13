# import tensorflow as tf
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# input("Press Enter to continue...")

class Vorjo_Vectorizer:

    def __init__(self, common_freq = 1, rare_freq = 0):
        self.vocabulary = {}
        self.cut_vocab = {}
        self.tf = []
        self.common_freq = common_freq
        self.rare_freq = rare_freq

    def fit(self, doc):
        word_list = doc.split()
        for word_index in range(len(word_list)):
            new_word = ""
            for char in word_list[word_index]:
                if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-''":
                    new_word += char.lower()
            if len(new_word.strip()) > 0:
                word_list[word_index] = new_word.strip()

        for word in word_list:
            if word in self.vocabulary:
                self.tf[self.vocabulary[word]] += 1
            else:
                self.vocabulary[word] = len(self.tf)
                self.tf.append(1)
        length = np.linalg.norm(self.tf)

        for i in range(len(self.tf)):
            self.tf[i] = self.tf[i]/length

        self.update_cut_vocab()

    def print_dict(self):
        for word in self.vocabulary:
            print(word)

    def print_cut_dict(self):
        for word in self.cut_vocab:
            print(word)

    def print_letter_frequency(self):
        for word in self.vocabulary:
            print(word + " " + str(self.tf[self.vocabulary[word]]))

    def print_letter_frequency_inv_order(self):
        new_vocab = dict(self.vocabulary)
        new_tf = self.tf[:]

        while len(new_vocab) > 0:
            min_freq = 1
            min_word = ""
            # print(len(new_vocab))
            for word in new_vocab:
                # print(word, new_tf[new_vocab[word]])
                if new_tf[new_vocab[word]] < min_freq:
                    min_freq = new_tf[new_vocab[word]]
                    min_word = word

            print(min_word + " " + str(min_freq))
            # del new_tf[new_vocab[word]]
            del new_vocab[min_word]

    def update_cut_vocab(self):
        new_vocab = {}
        for word in self.vocabulary:
            freq = self.tf[self.vocabulary[word]]
            if (freq < self.common_freq) and (freq > self.rare_freq):
                new_vocab[word] = self.vocabulary[word]
        self.cut_vocab = new_vocab

    def transform(self, doc):
        word_list = doc.split()
        for word_index in range(len(word_list)):
            new_word = ""
            for char in word_list[word_index]:
                if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-''":
                    new_word += char.lower()
            if len(new_word.strip()) > 0:
                word_list[word_index] = new_word.strip()

        vector = [0]*len(self.tf)
        for word in word_list:
            if word in self.cut_vocab:
                vector[self.cut_vocab[word]] += 1

        norm = np.linalg.norm(vector)

        return [i/norm for i in vector]
