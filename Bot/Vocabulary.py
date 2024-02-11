import string
from collections import Counter
import numpy as np


class Vocabulary:
    def __init__(self, texts: list[str], min_freq: int = 10):

        text = ' '.join(texts)  # превращаем все в строку с разделителем пробелом

        # удаляем все двойные пробелы на одинарные
        while '  ' in text:
            text = text.replace('  ', ' ')

        words = text.strip().lower().split()  # обрезаем по сторонам, приводим к нижнему регистру и сплитим по пробелам

        c = Counter(words)  # заводим счетчик слов

        # заносим в словарь все слова которые встречаются чаще, чем минимальная частота и дополнительный символ для неизвестных слов
        self.vocabulary = list(set([word for word in words if c[word] >= min_freq]))
        self.vocabulary.append('<unk>')
        # заведем словарь индекс: слово и слово: индекс
        self._idx2word = {i: word for i, word in enumerate(self.vocabulary)}
        self._word2idx = {word: i for i, word in enumerate(self.vocabulary)}

    def get_vocabulary(self):
        '''
            function for return vocabulary
        '''
        return self.vocabulary()

    def idx2word(self, idx: int):
        '''
            function for return a word by index
            params: int idx - index
            return: str - word
        '''
        # если такого индекса нет, то возвращаем <unk>
        if idx not in self._idx2word:
            return '<unk>'

        return self._idx2word[idx]

    def word2idx(self, word: str):
        '''
            function for return a index by word
            params: str word - word
            return: int - index
        '''
        word = word.lower()  # переводим слова в нижний регистр

        # если такого слова нет, вернем индекс <unk>
        if word not in self._word2idx:
            return self._word2idx['<unk>']

        return self._word2idx[word]

    def encode(self, text):
        '''
            function for encoding text
            params: text: str
            return: encoded list
        '''
        result = []
        text = text.lower()  # переводим текст в нижний регистр

        for word in text.split():  # проходимся по словам из списка
            if word in self._word2idx:  # если слово есть в словаре слов, добавляем значение этого слова
                result.append(self._word2idx[word])

        return result

    def build_vectors(self, fasttext):
        '''
            function for return vectors
            params: fasttext - a model that can return the text words of their vector
            return: stack array
        '''
        vectors = []

        for word in self.vocabulary:
            # если в нашей модели есть векторное представлние для этогго слова - добавляем
            if fasttext.has_index_for(word):
                vectors.append(fasttext[word])
            else:
                vectors.append(np.zeros(
                    25))  # иначе добавляем в вектор массив нулей размером 25, так как в fasttext размеры векторов 25

        return np.stack(vectors)  # возвращаем застаканный массив этих векторов