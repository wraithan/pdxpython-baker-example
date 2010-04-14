#!/usr/bin/env python
import string

import baker
# ^ - Most important thing to remember when using baker.

# "Gunaxf Qvfpbtf sbe gur cvmmn naq orre."

@baker.command
def rot13(text="", verbose=False):
    """ A command for your secretest secrets.

    :param text: The secret you need to hide or expose.
    :param verbose: The verbosity.
    """
    table = string.maketrans(
	'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM',
	'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if verbose:
        print "You entered: '%s', which translates to: " % text
    print string.translate(text, table)

baker.run()
