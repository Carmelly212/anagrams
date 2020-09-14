list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']


anagrams = []
temp_anagrams = []
singles = []

for word in list_of_words:
     temp_anagrams.clear()
     temp_anagrams.append(sorted(word))
for word_2 in list_of_words:
    if sorted(word_2) in temp_anagrams:
       anagrams.append(word_2)
    else:
       singles.append([word_2])

new = singles + [anagrams]

print (new)



