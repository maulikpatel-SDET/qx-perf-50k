"""Service module 20516: business logic, no crypto."""


def calculate_total_20516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20516():
    return 'module 20516 handles orders and invoices'
