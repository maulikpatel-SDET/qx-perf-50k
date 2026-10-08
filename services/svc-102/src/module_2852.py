"""Service module 2852: business logic, no crypto."""


def calculate_total_2852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2852():
    return 'module 2852 handles orders and invoices'
