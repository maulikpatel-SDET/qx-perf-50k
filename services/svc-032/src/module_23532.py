"""Service module 23532: business logic, no crypto."""


def calculate_total_23532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23532():
    return 'module 23532 handles orders and invoices'
