"""Service module 39061: business logic, no crypto."""


def calculate_total_39061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39061():
    return 'module 39061 handles orders and invoices'
