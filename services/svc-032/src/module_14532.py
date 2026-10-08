"""Service module 14532: business logic, no crypto."""


def calculate_total_14532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14532():
    return 'module 14532 handles orders and invoices'
