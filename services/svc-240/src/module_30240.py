"""Service module 30240: business logic, no crypto."""


def calculate_total_30240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30240():
    return 'module 30240 handles orders and invoices'
