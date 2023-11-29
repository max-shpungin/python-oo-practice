import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.
   # >>> wf = WordFinder("/usr/share/dict/words")
    >>> wf = WordFinder("words.txt")
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
        self.word_list = self.remove_new_lines(self.word_list)
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

    def remove_new_lines(self, word_list):
        """Takes a word_list and strips out new line chars"""
        clean_list = []
        for word in word_list:
            clean_list.append(word.strip())
        return clean_list


#need a new class that ignores blank lines and lines that start with #
class SpecialWordFinder(WordFinder):
    """Extends word finder to ignore blank lines and lines that start with #
    >>> wf = SpecialWordFinder("words.txt")
    9 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, path):
        super().__init__(path)
        self.word_list = self.remove_blanks_and_hashes(self.word_list)

    #we can reference the existing self.word_list
    #check if first char is space or hash and pop if so

    def remove_blanks_and_hashes(self, word_list):
        clean_list = []
        for line in word_list:
            if not (line.startswith(' ') and line.startswith('#')):
                clean_list.append(line)
        return clean_list
