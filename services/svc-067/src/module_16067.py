"""Service module 16067: business logic, no crypto."""


def calculate_total_16067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16067():
    return 'module 16067 handles orders and invoices'
