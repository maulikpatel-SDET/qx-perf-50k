"""Service module 19657: business logic, no crypto."""


def calculate_total_19657(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19657():
    return 'module 19657 handles orders and invoices'
