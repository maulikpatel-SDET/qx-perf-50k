"""Service module 11029: business logic, no crypto."""


def calculate_total_11029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11029():
    return 'module 11029 handles orders and invoices'
