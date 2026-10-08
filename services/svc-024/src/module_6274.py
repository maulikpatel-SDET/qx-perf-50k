"""Service module 6274: business logic, no crypto."""


def calculate_total_6274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6274():
    return 'module 6274 handles orders and invoices'
