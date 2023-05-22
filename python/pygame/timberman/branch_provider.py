from pgzero.builtins import Actor
import random
from static import HEIGHT, WIDTH, BASE_HEIGHT, BASE_WIDTH
from utils import scale_to

class BranchProvider:
    def __init__(self, screen):
        self.branch_count = 10
        self.screen = screen
        self.screen_width = self.screen.surface.get_size()[0]
        self.screen_height = self.screen.surface.get_size()[1]
        self.left_branches = [self.create_branch() for _ in range(self.branch_count)]
        self.right_branches = [self.create_branch(left=False) for _ in range(self.branch_count)]
        scale_to(self.all_branches(), (BASE_WIDTH, BASE_HEIGHT), (WIDTH, HEIGHT), change_pos=False)
        self.branches_in_game = []
        self.last_taken_left = 0
        self.last_taken_right = 0
        self.top = 0
        self.up_scale = 15 / 60
        self.create_game()

    def all_branches(self):
        return self.left_branches + self.right_branches

    def create_game(self):
        start_point = (33/60) * self.screen_height
        up = self.up_scale * self.screen_height
        for _ in range(self.branch_count):
            rand = random.randint(0, 2)
            if rand == 0:
                self.branches_in_game.append(None)
            if rand == 1:
                self.branches_in_game.append((self.left_branches[self.last_taken_left], 'left'))
                self.last_taken_left += 1
            if rand == 2:
                self.branches_in_game.append((self.right_branches[self.last_taken_right], 'right'))
                self.last_taken_right += 1
        for i, branch in enumerate(self.branches_in_game):
            self.top = start_point - i*up
            if branch is None:
                continue
            branch[0].y = self.top
        self.top = start_point - len(self.branches_in_game)*up

    def create_branch(self, left=True):
        branch_scale_left = 369/800
        branch_scale_right = 432/800
        branch_left_unused = Actor('konar_lewy')
        if left:
            branch = Actor('konar_lewy', pos=(branch_scale_left * WIDTH, -100), anchor=(branch_left_unused.width, 0))
        else:
            branch = Actor('konar_prawy', pos=(branch_scale_right * WIDTH, -100), anchor=(0, 0))
        return branch

    def branches_to_draw(self):
        branches = []
        for branch in self.branches_in_game:
            if branch is None:
                continue
            branches.append(branch[0])
        return branches

    def recalculate_screen(self):
        self.screen_width = self.screen.surface.get_size()[0]
        self.screen_height = self.screen.surface.get_size()[1]
        start_point = (33/60) * self.screen_height
        up = self.up_scale * self.screen_height
        self.top = start_point - len(self.branches_in_game) * up

    def add_branch(self):
        rand = random.randint(0, 2)
        if rand == 0:
            self.branches_in_game.append(None)
        if rand == 1:
            if self.last_taken_left == self.branch_count:
                self.last_taken_left = 0
            self.left_branches[self.last_taken_left].y = self.top
            self.branches_in_game.append((self.left_branches[self.last_taken_left], 'left'))
            self.last_taken_left += 1
        if rand == 2:
            if self.last_taken_right == self.branch_count:
                self.last_taken_right = 0
            self.right_branches[self.last_taken_right].y = self.top
            self.branches_in_game.append((self.right_branches[self.last_taken_right], 'right'))
            self.last_taken_right += 1

    def hit(self):
        self.recalculate_screen()
        self.add_branch()
        for branch in self.branches_in_game:
            if branch is not None:
                branch[0].y += self.up_scale * self.screen_height
        self.branches_in_game.pop(0)

    def collision(self, key):
        last = self.branches_in_game[0]
        if last is None:
            return False
        if last[1] == 'left' and key == 'left':
            return True
        if last[1] == 'right' and key == 'right':
            return True
        else:
            return False


