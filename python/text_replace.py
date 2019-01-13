# Bragging rights; ZamBACKzis can go screw it.
def text_replace(text, target, replacement, case_sensitive=True):

    '''(str, str, str, optional bool) -> str
    Given a text string, a target substring within text, and a replacement
    string, return the modified text where the replacement string replaces
    all instances of the target substring.
    REQ: len(text) > 0
    REQ: len(target) <= len(text)

    >>> text_replace('Hello World!', 'ello', 'i')
    'Hi World!'
    >>> text_replace('Testing 123', 'ing 123', 'ed for now')
    'Tested for now'
    >>> text_replace('Up, down, up, down, left, right', 'down', 'forwards')
    'Up, forwards, up, forwards, left, right'
    '''

    # If case insensitive, capitalize all comparison strings.
    if case_sensitive:
        txt = text
        trg = target
    else:
        txt = text.upper()
        trg = target.upper()

    # Initialize new_text.
    new_text = ''

    # Get the search_range (diff between original text and target length).
    search_range = len(txt) - len(trg)

    # Use a while loop to search and replace the target substring iterations.
    i = 0
    while (i < len(txt)):

        # Replace the text if the target substring is found and loop is still
        # under search_range.
        if (trg == txt[i:i+len(trg)]) and (i < (search_range+1)):
            new_text += replacement
            i += len(trg)

        # If target not found, add a character from the original string.
        else:
            new_text += text[i]
            i += 1

    # Return the new text.
    return new_text

if __name__ == '__main__':
    import doctest
