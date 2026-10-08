"""Service module 25870: business logic, no crypto."""


def calculate_total_25870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25870():
    return 'module 25870 handles orders and invoices'
