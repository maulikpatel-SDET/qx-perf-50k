"""Service module 25532: business logic, no crypto."""


def calculate_total_25532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25532():
    return 'module 25532 handles orders and invoices'
