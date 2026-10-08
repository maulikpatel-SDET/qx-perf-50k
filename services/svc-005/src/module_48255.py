"""Service module 48255: business logic, no crypto."""


def calculate_total_48255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48255():
    return 'module 48255 handles orders and invoices'
