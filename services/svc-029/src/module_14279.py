"""Service module 14279: business logic, no crypto."""


def calculate_total_14279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14279():
    return 'module 14279 handles orders and invoices'
