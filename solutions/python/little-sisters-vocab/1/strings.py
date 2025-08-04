"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    return (" :: " + vocab_words[0]).join(vocab_words)
def remove_suffix_ness(word):
    if word[-5] == "i":
        return word[:-5] + "y"
    else:
        return word[:-4]

def adjective_to_verb(sentence, index):
    return sentence[:-1].split()[index]+"en"