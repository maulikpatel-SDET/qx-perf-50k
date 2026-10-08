"""Service module 48449: business logic, no crypto."""


def calculate_total_48449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48449():
    return 'module 48449 handles orders and invoices'
