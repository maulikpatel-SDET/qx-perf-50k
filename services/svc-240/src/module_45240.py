"""Service module 45240: business logic, no crypto."""


def calculate_total_45240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45240():
    return 'module 45240 handles orders and invoices'
