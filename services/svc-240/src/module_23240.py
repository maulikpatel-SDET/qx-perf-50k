"""Service module 23240: business logic, no crypto."""


def calculate_total_23240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23240():
    return 'module 23240 handles orders and invoices'
