"""Service module 17449: business logic, no crypto."""


def calculate_total_17449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17449():
    return 'module 17449 handles orders and invoices'
