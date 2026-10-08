"""Service module 18852: business logic, no crypto."""


def calculate_total_18852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18852():
    return 'module 18852 handles orders and invoices'
