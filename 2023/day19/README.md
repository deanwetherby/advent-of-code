# day 19

Part workflows

## part 1

Workflow conditions seem like they could be evaluated using `eval()`

```python
>>> x = 7
>>> rule = "x>5"
>>> eval(rule)
True
```

## part 2

Each part attribute ranges from 1 to 4000. That is too many combinations to make forward passes for each.

Could pivot on the workflows working backwards from accepted conditions. I would get a list of conditions per attributes that works for that particular workflow.

Or I could use ranges as input and then change the range at each condition. Seems easier.
