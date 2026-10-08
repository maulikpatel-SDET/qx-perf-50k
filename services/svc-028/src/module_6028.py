"""Service module 6028: business logic, no crypto."""


def calculate_total_6028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6028():
    return 'module 6028 handles orders and invoices'
