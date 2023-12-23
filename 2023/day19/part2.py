import math

with open("input.txt") as f:
    data = f.read().split("\n\n")

workflows = {}
for wf in data[0].splitlines():
    key, val = wf.split("{")
    rules = val[:-1].split(",")
    rules = [tuple(rule.split(":")) for rule in rules]
    workflows[key] = rules

part = {
    "x": range(1,4000),
    "m": range(1,4000),
    "a": range(1,4000),
    "s": range(1,4000),
}


def filter_parts(workflows, lst):

    while lst:
        f, p = lst.pop()
        if f == "A":
            yield math.prod(len(r)+1 for r in p.values())
        elif f != "R":
            for r in workflows.get(f):
                if len(r) == 2:
                    component, operand, val = r[0][0], r[0][1], int(r[0][2:])
                    next_workflow = r[1]
                else:
                    next_workflow = r[0]
                    lst.append((next_workflow, p.copy()))
                    continue

                rr = p.get(component)
                if operand == ">":
                    p[component] = range(1+max(rr.start, val), rr.stop)
                    lst.append((next_workflow, p.copy()))
                    p[component] = range(rr.start, min(rr.stop, val))
                elif operand == "<":
                    p[component] = range(rr.start, min(rr.stop, val)-1)
                    lst.append((next_workflow, p.copy()))
                    p[component] = range(max(rr.start, val), rr.stop)


print(sum(filter_parts(workflows, [("in", part)])))
