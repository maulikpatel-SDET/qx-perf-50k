"""Service module 48474: business logic, no crypto."""


def calculate_total_48474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48474():
    return 'module 48474 handles orders and invoices'
