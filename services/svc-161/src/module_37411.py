"""Service module 37411: business logic, no crypto."""


def calculate_total_37411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37411():
    return 'module 37411 handles orders and invoices'
