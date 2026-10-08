"""Service module 41451: business logic, no crypto."""


def calculate_total_41451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41451():
    return 'module 41451 handles orders and invoices'
