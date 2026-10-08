"""Service module 29852: business logic, no crypto."""


def calculate_total_29852(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29852():
    return 'module 29852 handles orders and invoices'
