"""Service module 17836: business logic, no crypto."""


def calculate_total_17836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17836():
    return 'module 17836 handles orders and invoices'
