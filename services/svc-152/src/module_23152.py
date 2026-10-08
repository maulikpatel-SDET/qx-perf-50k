"""Service module 23152: business logic, no crypto."""


def calculate_total_23152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23152():
    return 'module 23152 handles orders and invoices'
