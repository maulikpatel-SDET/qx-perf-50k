"""Service module 28833: business logic, no crypto."""


def calculate_total_28833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28833():
    return 'module 28833 handles orders and invoices'
