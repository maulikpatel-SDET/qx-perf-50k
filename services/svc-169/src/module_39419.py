"""Service module 39419: business logic, no crypto."""


def calculate_total_39419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39419():
    return 'module 39419 handles orders and invoices'
