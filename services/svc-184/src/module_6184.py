"""Service module 6184: business logic, no crypto."""


def calculate_total_6184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6184():
    return 'module 6184 handles orders and invoices'
