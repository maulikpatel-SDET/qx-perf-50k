"""Service module 13880: business logic, no crypto."""


def calculate_total_13880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13880():
    return 'module 13880 handles orders and invoices'
