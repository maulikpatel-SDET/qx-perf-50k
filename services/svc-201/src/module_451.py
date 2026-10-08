"""Service module 451: business logic, no crypto."""


def calculate_total_451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_451():
    return 'module 451 handles orders and invoices'
