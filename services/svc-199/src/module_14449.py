"""Service module 14449: business logic, no crypto."""


def calculate_total_14449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14449():
    return 'module 14449 handles orders and invoices'
