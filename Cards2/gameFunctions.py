def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def display_options(options):
  index = 1
  for option in options:
    print(str.format('{}......{}',index,option))
    index+=1
  while True:
    choice = input('pick an number between 1 and'+str(len(options))+":")
    if choice.isnumeric():
      choice = int(choice)
      if choice >= 1 and choice <= len(options):
        return choice
      else:
        print('Not an option')
    else:
        print('Not an option')

class Player(object):
    def __init__(self,name):
        self.name = name
        self.score = Score()
        self.isAlive = True
        self.lives = 3

class Score(object):
    def __init__(self):
        self.score = 0

    def add_to_score(self, points):
        self.score += points

    def take_points(self,points):
        self.score -= points
        if self.score < 0:
            self.score = 0

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")