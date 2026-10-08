"""Service module 33061: business logic, no crypto."""


def calculate_total_33061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33061():
    return 'module 33061 handles orders and invoices'
