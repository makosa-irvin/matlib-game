#the code should mimick a madlib game
#there are different type of words
#the words are chosen randomly to fit a story

from random import randint
import copy
#the story with blanks

story = ('I am {} a {} party for my birthday.' + 'I am {} my best friends, like {} and {} and {}.' + ' The party will be at the {}'
         ' with {} {} and {} {} for decorations. ' +
         ' First, we will {} some snacks,like {} and {}, and then we will {} some party games' +
         ' Then comes my favourite part: {} Happy Birthday, {} presents' +
         'and {} some {} cake ')


#the words in the blanks
words_dict = {'name': ['Jake','Mike','Britta','Leo','Hope'],
              'verb': ['eat','drink','meet','greet','cook'],
              'verb-ing': ['attending','singing','cutting','hosting','inviting'],
              'adjective': ['beautiful','great','tasty','awesome','some','a lot of'],
              'color': ['green','red','pink','blue'],
              'place': ['hotel','backyard','restaurant'],
              'plural noun': ['balloons','stripes','piniatas'],
              'food': ['Chips','Popcorns','Oreo','Candy']}

#functions to get word
def fill_blank(type, local_dict):
    choices = local_dict[type]
    counter = len(choices) - 1
    index = randint(0,counter)
    return local_dict[type].pop(index)




def make_story():
    local_dict = copy.deepcopy(words_dict)
    return story.format(
        fill_blank('verb-ing', local_dict),
        fill_blank('adjective', local_dict),
        fill_blank('verb-ing', local_dict),
        fill_blank('name', local_dict),
        fill_blank('name', local_dict),
        fill_blank('name', local_dict),
        fill_blank('place', local_dict),
        fill_blank('adjective', local_dict),
        fill_blank('plural noun', local_dict),
        fill_blank('color', local_dict),
        fill_blank('plural noun', local_dict),
        fill_blank('verb', local_dict),
        fill_blank('food', local_dict),
        fill_blank('food', local_dict),
        fill_blank('verb', local_dict),
        fill_blank('verb-ing', local_dict),
        fill_blank('verb-ing', local_dict),
        fill_blank('verb-ing', local_dict),
        fill_blank('adjective', local_dict)

    )
print(make_story())