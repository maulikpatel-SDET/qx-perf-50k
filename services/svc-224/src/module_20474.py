"""Service module 20474: business logic, no crypto."""


def calculate_total_20474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20474():
    return 'module 20474 handles orders and invoices'
