"""Service module 37222: business logic, no crypto."""


def calculate_total_37222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37222():
    return 'module 37222 handles orders and invoices'
