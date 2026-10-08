"""Service module 28449: business logic, no crypto."""


def calculate_total_28449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28449():
    return 'module 28449 handles orders and invoices'
