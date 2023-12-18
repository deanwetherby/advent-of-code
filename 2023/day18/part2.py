
with open("input.txt") as f:
    data = f.read().splitlines()

dig_path = []
for line in data:
    dig_path.append(line.split(" "))

movement = {
    "0": complex(1, 0),
    "2": complex(-1, 0),
    "3": complex(0, -1),
    "1": complex(0, 1),
}

vertices = [complex(0,0)]
boundary = 0
for _, _, p in dig_path:
    amount = int("0x" + p[2:-2], 0)
    mv = p[-2]
    boundary += amount
    vertices.append(vertices[-1] + (amount * movement.get(mv)))


def picks(area: int, boundary: int) -> int:
    """Pick's Theorem. Returns number of interior cells"""
    return area - boundary // 2 + 1


def shoelace(vertices: list[complex]) -> int:
    """Shoelace formula
    Args:
        vertices: list of closed loop vertices
    Returns:
        area: integer
    """
    sum1, sum2 = 0, 0
    for i in range(len(vertices) - 1):
        sum1 = sum1 + vertices[i].real * vertices[i+1].imag
        sum2 = sum2 + vertices[i].imag * vertices[i+1].real
    return abs(sum1 - sum2) / 2


area = shoelace(vertices)
interior = picks(area, boundary)
print(boundary + interior)
