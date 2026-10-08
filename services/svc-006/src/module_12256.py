"""Service module 12256: business logic, no crypto."""


def calculate_total_12256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12256():
    return 'module 12256 handles orders and invoices'
