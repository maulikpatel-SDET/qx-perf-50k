"""Service module 41870: business logic, no crypto."""


def calculate_total_41870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41870():
    return 'module 41870 handles orders and invoices'
