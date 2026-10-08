"""Service module 11449: business logic, no crypto."""


def calculate_total_11449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11449():
    return 'module 11449 handles orders and invoices'
