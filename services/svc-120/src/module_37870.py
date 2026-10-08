"""Service module 37870: business logic, no crypto."""


def calculate_total_37870(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37870():
    return 'module 37870 handles orders and invoices'
