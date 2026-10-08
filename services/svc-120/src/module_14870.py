"""Service module 14870: business logic, no crypto."""


def calculate_total_14870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14870():
    return 'module 14870 handles orders and invoices'
