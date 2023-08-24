#capture words from the user for mad libs
plural_nouns = input('Choose a nous that is plural: ')
verb1 = input ('Choose a verb: ')
verb2 = input ('Choose a verb: ')
verb3 = input ('Choose a verb: ')
adjective = input('Chose an adjective: ')
noun = input('Choose a noun: ')
exclamation = input('Choose a word to yell: ')

#story:
'''
The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.

Make sure to match the punctuation and spacing of the original story exactly (for example, you should not put your words on their own line, they should fit naturally into the story).

Also, make it so that the "exclamation" word is automatically capitalized, because it starts a new sentence.
'''
print(f'\nThe other day, I was really in trouble. It all started when I saw a very\n {adjective} animal {verb1} down the hallway.\n\
"{exclamation.upper()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously,\n\
that caused it to stop, but not before it tried to {verb3} right in front of my family.\n')