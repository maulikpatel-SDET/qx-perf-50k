"""Service module 18870: business logic, no crypto."""


def calculate_total_18870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18870():
    return 'module 18870 handles orders and invoices'
