"""Service module 7240: business logic, no crypto."""


def calculate_total_7240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7240():
    return 'module 7240 handles orders and invoices'
