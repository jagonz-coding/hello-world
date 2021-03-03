#Name: Juan Gonzalez
#ID: 1808943

class Team:
    def __init__(self):
        self.name = ''
        self.wins = 0
        self.losses = 0

    def get_team_name(self, name):
        self.name = name

    def get_team_wins(self, wins):
        self.wins = wins

    def get_team_losses(self, losses):
        self.losses = losses

    def get_win_percentage(self):
        percent = self.wins / (self.wins + self.losses)
        return percent


if __name__ == "__main__":

    t = Team()

    name = input()
    wins = int(input())
    losses = int(input())

    t.get_team_name(name)
    t.get_team_wins(wins)
    t.get_team_losses(losses)

    if t.get_win_percentage() >= 0.5:
        print('Congratulations, Team', t.name, 'has a winning average!')
    else:
        print('Team', t.name, 'has a losing average.')