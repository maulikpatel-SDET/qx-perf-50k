"""Service module 13081: business logic, no crypto."""


def calculate_total_13081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13081():
    return 'module 13081 handles orders and invoices'
