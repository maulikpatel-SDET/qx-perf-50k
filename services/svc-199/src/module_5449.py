"""Service module 5449: business logic, no crypto."""


def calculate_total_5449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5449():
    return 'module 5449 handles orders and invoices'
