"""Service module 24564: business logic, no crypto."""


def calculate_total_24564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24564():
    return 'module 24564 handles orders and invoices'
