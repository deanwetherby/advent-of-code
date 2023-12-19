with open("input.txt") as f:
    data = f.read().split("\n\n")

parts = []
for part in data[1].splitlines():
    components = part[1:-1].split(",")
    comps = [c for comp in components for c in comp.split("=")]
    d = {k: v for k, v in zip(comps[::2], comps[1::2])}
    parts.append(d)

workflows = {}
for wf in data[0].splitlines():
    key, val = wf.split("{")
    rules = val[:-1].split(",")
    rules = [tuple(rule.split(":")) for rule in rules]
    workflows[key] = rules


def apply_rule(part, rule, workflows) -> int:
    # get part attributes into local variables for `eval`
    x, m, a, s = (int(part[k]) for k in ("x", "m", "a", "s"))
    for r in rule:
        res = None
        if len(r) == 1:
            res = r[0]
        else:
            if eval(r[0]):
                res = r[1]
            else:
                continue
        if res == "A":
            return sum([x, m, a, s])
        elif res == "R":
            return 0
        else:
            return apply_rule(part, workflows.get(res), workflows)


print(sum(apply_rule(part, workflows.get("in"), workflows) for part in parts))
