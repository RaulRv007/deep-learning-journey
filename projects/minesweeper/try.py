from minesweeper import Sentence
mySentence = Sentence({(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)}, 3)


mySentence.mark_mine((0, 1))
mySentence.mark_mine((0, 3))
mySentence.mark_mine((0, 5))

print(mySentence.known_mines())