"""Service module 40474: business logic, no crypto."""


def calculate_total_40474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40474():
    return 'module 40474 handles orders and invoices'
