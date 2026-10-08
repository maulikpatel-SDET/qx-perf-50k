"""Service module 39184: business logic, no crypto."""


def calculate_total_39184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39184():
    return 'module 39184 handles orders and invoices'
