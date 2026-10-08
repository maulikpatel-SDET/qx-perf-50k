"""Service module 18474: business logic, no crypto."""


def calculate_total_18474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18474():
    return 'module 18474 handles orders and invoices'
