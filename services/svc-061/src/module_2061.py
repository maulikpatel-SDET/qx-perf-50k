"""Service module 2061: business logic, no crypto."""


def calculate_total_2061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2061():
    return 'module 2061 handles orders and invoices'
