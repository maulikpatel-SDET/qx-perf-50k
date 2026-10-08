"""Service module 29449: business logic, no crypto."""


def calculate_total_29449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29449():
    return 'module 29449 handles orders and invoices'
