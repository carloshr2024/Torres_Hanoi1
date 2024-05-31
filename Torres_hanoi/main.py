import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def draw_tower(ax, positions, disks):
    ax.clear()
    ax.set_xlim(-2, 10)
    ax.set_ylim(0, len(disks) + 1)
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'grey', 'cyan']

    # Draw base and poles
    ax.add_patch(patches.Rectangle((-1, 0), 12, 0.5, facecolor='saddlebrown'))
    for i in range(3):
        ax.add_patch(patches.Rectangle((i * 3 + 1, 0.5), 0.2, len(disks), facecolor='black'))

    # Draw disks
    for i, pole in enumerate(positions):
        for j, disk in enumerate(pole):
            x = i * 3 + 1 - disks[disk] / 2
            y = j + 1
            ax.add_patch(patches.Rectangle((x, y), disks[disk], 0.8, facecolor=colors[disk % len(colors)]))

    plt.pause(0.5)

def move_disk(positions, from_pole, to_pole):
    disk = positions[from_pole].pop()
    positions[to_pole].append(disk)

def solve_hanoi(positions, disks, n, from_pole, to_pole, aux_pole, ax):
    if n == 1:
        move_disk(positions, from_pole, to_pole)
        draw_tower(ax, positions, disks)
        return
    solve_hanoi(positions, disks, n - 1, from_pole, aux_pole, to_pole, ax)
    move_disk(positions, from_pole, to_pole)
    draw_tower(ax, positions, disks)
    solve_hanoi(positions, disks, n - 1, aux_pole, to_pole, from_pole, ax)

def main():
    config = load_config()
    num_disks = config['discs']

    # Initialize positions of disks
    positions = [list(range(num_disks - 1, -1, -1)), [], []]
    disks = [0.9 + 0.5 * i for i in range(num_disks)]

    fig, ax = plt.subplots()
    draw_tower(ax, positions, disks)
    solve_hanoi(positions, disks, num_disks, 0, 2, 1, ax)
    plt.show()

if __name__ == "__main__":
    main()
