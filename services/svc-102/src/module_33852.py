"""Service module 33852: business logic, no crypto."""


def calculate_total_33852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33852():
    return 'module 33852 handles orders and invoices'
