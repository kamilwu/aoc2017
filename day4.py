def get_valid_passphrases():
    with open("data/day4") as f:
        no_duplicates = 0
        no_anagrams = 0
        for line in f:
            words = line.rstrip().split(' ')
            # Check for duplicates
            if len(set(words)) == len(words):
                no_duplicates += 1
            # Check for anagrams
            sorted_chars = [''.join(sorted(x)) for x in words]
            if len(set(sorted_chars)) == len(words):
                no_anagrams += 1
        return no_duplicates, no_anagrams


if __name__ == "__main__":
    print(get_valid_passphrases())
