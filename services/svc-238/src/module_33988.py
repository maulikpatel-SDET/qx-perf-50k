"""Service module 33988: business logic, no crypto."""


def calculate_total_33988(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33988():
    return 'module 33988 handles orders and invoices'
