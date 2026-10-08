"""Service module 6474: business logic, no crypto."""


def calculate_total_6474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6474():
    return 'module 6474 handles orders and invoices'
