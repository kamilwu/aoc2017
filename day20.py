import re


class Particle:
    def __init__(self, data):
        self.pos = data[:3]
        self.vel = data[3:6]
        self.acc = data[6:]

    def iterate(self):
        self.vel = [x + y for x, y in zip(self.vel, self.acc)]
        self.pos = [x + y for x, y in zip(self.pos, self.vel)]

    def distance(self):
        return sum(map(abs, self.pos))


def closest(particles):
    distances = [x.distance() for x in particles]
    return distances.index(min(distances))


with open("data/day20") as f:
    particles = []
    for line in f:
        numbers = re.findall(r'-?\d+', line)
        particles.append(Particle([int(x) for x in numbers]))

    for _ in range(1000):
        positions = [p.pos for p in particles]
        particles = [part for part, pos in zip(
            particles, positions) if positions.count(pos) == 1]
        for p in particles:
            p.iterate()
    print(len(particles))
