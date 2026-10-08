"""Service module 39321: business logic, no crypto."""


def calculate_total_39321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39321():
    return 'module 39321 handles orders and invoices'
