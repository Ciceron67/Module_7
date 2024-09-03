class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = list(file_name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    i.replace(i, '')
            words = text.split()
            all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        pos = {}
        for fname, value in self.get_all_words().items():
            if word in value:
                pos[fname] = value.index(word) + 1
        return pos

    def count(self, word):
        word = word.lower()
        pos = {}
        for fname, value in self.get_all_words().items():
            if word in value:
                pos[fname] = value.count(word)
        return pos


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
