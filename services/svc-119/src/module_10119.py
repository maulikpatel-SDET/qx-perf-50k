"""Service module 10119: business logic, no crypto."""


def calculate_total_10119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10119():
    return 'module 10119 handles orders and invoices'
