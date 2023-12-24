import z3
# python -m pip install z3-solver

hail = [[int(i) for i in l.replace('@',',').split(',')]
                for l in open('input.txt')]

rock = z3.RealVector('r', 3)
vel = z3.RealVector('v', 3)
time = z3.RealVector('t', 3)

s = z3.Solver()
s.add(*[rock[d] + vel[d] * t == hail[d] + hail[d+3] * t
        for t, hail in zip(time, hail) for d in range(3)])
s.check()

print(s.model().eval(sum(rock[:3])))
