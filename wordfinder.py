import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> wf = WordFinder("/usr/share/dict/words")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    #instantiated with a path to a file on disk that contains words, one word per line
    def __init__ (self, path):
        """ Read file and make a list of words.
          Output number of words in the file"""

        txt_file = open(path)
        self.word_list = self.get_words_from_file(txt_file)
        txt_file.close()

        print(f"{len(self.word_list)} words read")

    def get_words_from_file(self, txt_file):
        """Accepts file. Returns list of lines"""
        word_list=[]

        for line in txt_file:
            word_list.append(line)

        return word_list

    def random(self):
        """Returns random word."""
        return random.choice(self.word_list)

