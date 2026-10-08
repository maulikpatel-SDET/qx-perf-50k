"""Service module 40852: business logic, no crypto."""


def calculate_total_40852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40852():
    return 'module 40852 handles orders and invoices'
