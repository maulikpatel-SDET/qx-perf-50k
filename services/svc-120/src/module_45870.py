"""Service module 45870: business logic, no crypto."""


def calculate_total_45870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45870():
    return 'module 45870 handles orders and invoices'
