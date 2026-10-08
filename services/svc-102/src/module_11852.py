"""Service module 11852: business logic, no crypto."""


def calculate_total_11852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11852():
    return 'module 11852 handles orders and invoices'
