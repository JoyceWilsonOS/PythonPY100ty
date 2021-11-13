def get_list_of_longest_rotated_from_line(str_):
    words = str_.split()
    longest_word = max(words, key=len)
    longest_word_count = words.count(longest_word)
    if longest_word_count == 1:
        return longest_word[::-1]
    else:
        return [longest_word[::-1]] * longest_word_count
    # return max(str_.split(), key=len)[::-1] это не работает

if __name__ == "__main__":
    print(get_list_of_longest_rotated_from_line('sts abcdefg  abcdefg sdf a a         b    b   c'))
