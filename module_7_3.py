import string


class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()

                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(symbol, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            try:
                position = words.index(word)
                word_positions[name] = position + 1
            except ValueError:
                word_positions[name] = None

        return word_positions

    def count(self, word):
        word = word.lower()
        word_count = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            count = words.count(word)
            word_count[name] = count

        return word_count


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


finder1 = WordsFinder('if.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))