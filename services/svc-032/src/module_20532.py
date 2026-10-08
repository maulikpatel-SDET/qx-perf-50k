"""Service module 20532: business logic, no crypto."""


def calculate_total_20532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20532():
    return 'module 20532 handles orders and invoices'
