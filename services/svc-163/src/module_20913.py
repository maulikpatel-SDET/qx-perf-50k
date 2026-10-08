"""Service module 20913: business logic, no crypto."""


def calculate_total_20913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20913():
    return 'module 20913 handles orders and invoices'
