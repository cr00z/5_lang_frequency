import argparse
import collections
import os


NUM_OF_WORDS = 10


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='script for frequency analysis of words in any text')
    parser.add_argument('text_filename', metavar='text_filename', type=str,
                        help='text filename')
    return parser.parse_args()


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, encoding='utf-8') as text_file_object:
        return text_file_object.read()


def get_most_frequent_words(input_text):
    counted_words = collections.Counter()
    for word in input_text:
        if word > '@':
            counted_words[word] += 1
    return counted_words.most_common(NUM_OF_WORDS)


if __name__ == '__main__':
    args = get_cmdline_args()
    loaded_text = load_data(args.text_filename)
    if loaded_text is None:
        exit('we\'re really looking for your file to open, but didn\'t find it')
    most_frequent_words = get_most_frequent_words(loaded_text.split())
    for word, frequency in most_frequent_words:
        print("frequency: {}, word: {}".format(frequency, word))
