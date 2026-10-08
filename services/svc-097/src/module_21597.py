"""Service module 21597: business logic, no crypto."""


def calculate_total_21597(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21597():
    return 'module 21597 handles orders and invoices'
