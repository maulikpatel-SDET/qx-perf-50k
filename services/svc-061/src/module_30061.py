"""Service module 30061: business logic, no crypto."""


def calculate_total_30061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30061():
    return 'module 30061 handles orders and invoices'
