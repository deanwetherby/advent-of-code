import logging
import pathlib
import sys

from collections import namedtuple
from dataclasses import dataclass
from itertools import combinations


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

Position3 = namedtuple("Position3", ["x", "y", "z"])
Velocity3 = namedtuple("Velocity3", ["dx", "dy", "dz"])


@dataclass
class Hail:
    pos: Position3
    vel: Velocity3


def read_data(input: pathlib.Path) -> list[str]:
    return input.read_text().splitlines()


def parse_data(data: list[str]) -> list[Hail]:
    hailstones = []
    for line in data:
        line = line.replace(" ", "")
        position, velocity = line.split("@")
        x,y,z = list(map(int, position.split(",")))
        dx,dy,dz = list(map(int, velocity.split(",")))
        hailstones.append(Hail(Position3(x,y,z), Velocity3(dx,dy,dz)))
    return hailstones


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=pathlib.Path, default="input.txt")
    args = parser.parse_args()
    logger.info(args)
    data = read_data(args.input)
    hailstones = parse_data(data)

    TEST_AREA = range(200_000_000_000_000, 400_000_000_000_000)
    answer = 0
    for A, B in combinations(hailstones, 2):
        try:
            det = (B.vel.dx * A.vel.dy - B.vel.dy * A.vel.dx)
            u = ((B.pos.y - A.pos.y) * B.vel.dx - (B.pos.x - A.pos.x) * B.vel.dy) / det
            v = ((B.pos.y - A.pos.y) * A.vel.dx - (B.pos.x - A.pos.x) * A.vel.dy) / det

            if u < 0 or v < 0:
                continue
            t = B.pos.x + B.vel.dx * v
            s = B.pos.y + B.vel.dy * v

            if int(t) in TEST_AREA and int(s) in TEST_AREA:
                answer += 1
        except:
            pass

    print(answer)
