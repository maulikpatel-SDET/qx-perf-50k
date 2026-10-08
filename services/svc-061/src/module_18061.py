"""Service module 18061: business logic, no crypto."""


def calculate_total_18061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18061():
    return 'module 18061 handles orders and invoices'
