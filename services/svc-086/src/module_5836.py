"""Service module 5836: business logic, no crypto."""


def calculate_total_5836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5836():
    return 'module 5836 handles orders and invoices'
