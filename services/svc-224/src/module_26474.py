"""Service module 26474: business logic, no crypto."""


def calculate_total_26474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26474():
    return 'module 26474 handles orders and invoices'
