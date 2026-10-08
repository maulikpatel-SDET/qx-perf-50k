"""Service module 10274: business logic, no crypto."""


def calculate_total_10274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10274():
    return 'module 10274 handles orders and invoices'
