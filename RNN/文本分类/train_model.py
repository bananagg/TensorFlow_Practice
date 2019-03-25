import numpy
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

import tensorflow as tf


class SequenceClassificationModel:
    def __init__(self, data, target, params):
        self.data = data
        self.target = target
        self.params = params
        self.prediction
        self.cost
        self.error
        self.optimize

        pass

    def length(self):
        pass


    def prediction(self):
        pass

    def cost(self):
        pass

    def error(self):
        pass

    def optimize(self):
        pass


