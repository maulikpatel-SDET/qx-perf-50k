"""Service module 47061: business logic, no crypto."""


def calculate_total_47061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47061():
    return 'module 47061 handles orders and invoices'
