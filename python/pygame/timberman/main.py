import screeninfo

from static import *
from bee_behaviour import BeeAnimation
from branch_provider import BranchProvider
from utils import scale_to, bring_back_slice_wood
import time

bee_anim: Optional[BeeAnimation] = None
branches: Optional[BranchProvider] = None

scale_to(SCALABLE, (BASE_WIDTH, BASE_HEIGHT), (WIDTH, HEIGHT), change_pos=False)

hit = False
hit_time = time.time()
lumberjack_on_left = True
collision = False
time_left = 5
last_time = 0
score = 0
end_by_time = False
play = False

def reset():
    global collision, hit, hit_time, lumberjack_on_left, score, time_left, play, last_time, end_by_time
    score = 0
    time_left = 5
    last_time = 0
    collision = False
    end_by_time = False
    hit = False

def on_key_down(key):
    global hit, hit_time, lumberjack_on_left, collision, time_left, score, play
    if key == keys.RETURN:
        sounds.enter.play()
        if not play:
            play = True
        else:
            reset()

    if key == keys.F:
        if is_fullscreen():
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            scale_to(SCALABLE, surface_size, (WIDTH, HEIGHT))
            scale_to(branches.all_branches(), surface_size, (WIDTH, HEIGHT))
        else:
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
            scale_to(SCALABLE, surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT))
            scale_to(branches.all_branches(), surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT))
        change_fullscreen()

    if not play:
        return

    if not collision:
        if key == keys.LEFT:
            collision = branches.collision('left')
        elif key == keys.RIGHT:
            collision = branches.collision('right')
        if collision:
            sounds.fail.play()

    if collision:
        return

    width, height = screen.surface.get_size()[0], screen.surface.get_size()[1]
    if key == keys.LEFT:
        animate(slice_wood, on_finished=bring_back_slice_wood, duration=0.09, pos=(width, height/2))
    if key == keys.RIGHT:
        animate(slice_wood, on_finished=bring_back_slice_wood, duration=0.09, pos=(0, height/2))

    if key == keys.LEFT or key == keys.RIGHT:
        hit = True
        hit_time = time.time()
        sounds.hit.play()
        score += 1
        branches.hit()


        if score % 1000 == 0:
            time_left += 5
            sounds.power_up.play()
        if score < 1000:
            time_left += 2/score + 0.18
        if 1000 < score < 2000:
            time_left += 2/score + 0.15
        if 2000 < score < 4000:
            time_left += 2/score + 0.14
        if 4000 < score < 8000:
            time_left += 2/score + 0.135
        if score > 8000:
            time_left += 2/score + 0.129

    if key == keys.LEFT and not lumberjack_on_left:
        lumberjack_ready.flip(True, False)
        lumberjack_hit.flip(True, False)
        lumberjack_on_left = True
        lumberjack_ready.x -= 3.44 * trunk.width
        lumberjack_hit.x -= 2 * trunk.width

    if key == keys.RIGHT and lumberjack_on_left:
        lumberjack_ready.flip(True, False)
        lumberjack_hit.flip(True, False)
        lumberjack_on_left = False
        lumberjack_ready.x += 3.44 * trunk.width
        lumberjack_hit.x += 2 * trunk.width

def update():
    global bee_anim, hit, hit_time, branches, last_time, time_left, end_by_time, collision
    if not bee_anim:
        bee_anim = BeeAnimation(screen)
        bee_anim.animate_bee()
    if not branches:
        branches = BranchProvider(screen)

    screen_width = screen.surface.get_size()[0]
    for i, cloud in enumerate(clouds):
        cloud.x += cloud_speed[i]*(screen_width/BASE_WIDTH)
        if cloud.x > screen_width:
            cloud.x = -cloud.width

    if not play:
        return

    if hit:
        if time.time() - hit_time > 0.1:
            hit = False

    now = time.time()
    if not last_time:
        last_time = now
    delta_time = now - last_time
    time_left -= delta_time
    last_time = now

    if time_left < 0 and not collision:
        time_left = 0
        collision = True
        end_by_time = True

def draw():
    screen.fill(BLACK)
    width, height = screen.surface.get_size()[0], screen.surface.get_size()[1]
    background.draw()

    for cloud in clouds:
        cloud.draw()
    bee.draw()

    if not play:
        screen.draw.text('Naciśnij Enter \n aby zacząć lub zresetować', center=(width/2, height/2), color=GREEN, fontsize=40*(width/800)
                         ,fontname='bungee-regular', shadow=(1, 1))
        return

    if hit:
        trunk_base.draw()
        slice_wood.draw()
        trunk.draw()
        if not collision:
            lumberjack_hit.draw()
    else:
        tree.draw()
        if not collision:
            lumberjack_ready.draw()

    for branch in branches.branches_to_draw():
        branch.draw()

    if collision:
        if not end_by_time:
            screen.draw.text('Przegrałeś!', center=(width/2, height/2), color = GREEN, fontsize = 50*(width/800), fontname='bungee-regular',
                         shadow = (1, 1))
        else:
            screen.draw.text('Koniec czasu!', center=(width/2, height/2), color=GREEN, fontsize=50 * (width / 800),
                             fontname='bungee-regular' ,shadow=(1, 1))
        rip.draw()

    if not collision:
        lenght = 10*time_left
        rect = Rect(width/2 - lenght/2, height - 20 * height/450 - 20, lenght, 20 * height/450)
        screen.draw.filled_rect(rect, color=RED)

    screen.draw.text(f'Wynik: {score}', color=GREEN, fontsize=20 * (width/800), fontname='bungee-regular', shadow=(1, 1), topright=(width, 0) )

pgzrun.go()

