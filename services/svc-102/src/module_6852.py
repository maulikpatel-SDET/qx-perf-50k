"""Service module 6852: business logic, no crypto."""


def calculate_total_6852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6852():
    return 'module 6852 handles orders and invoices'
