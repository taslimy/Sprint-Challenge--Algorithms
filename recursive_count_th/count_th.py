'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  if not word: # personal note: an empty string will return false.
        return 0
  return (1 if word.startswith('th') else 0) + count_th(word[1:])
    # TBC

# checking if it works #
#test_one = "abcthxyzththth" #should be 4
#test_two = "thhtthhtsdfthnsmthmathnth" # should be 6

#print(count_th(test_one), count_th(test_two))