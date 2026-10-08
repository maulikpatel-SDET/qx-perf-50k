"""Service module 10874: business logic, no crypto."""


def calculate_total_10874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10874():
    return 'module 10874 handles orders and invoices'
