"""Service module 30527: business logic, no crypto."""


def calculate_total_30527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30527():
    return 'module 30527 handles orders and invoices'
