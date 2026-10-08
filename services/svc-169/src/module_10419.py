"""Service module 10419: business logic, no crypto."""


def calculate_total_10419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10419():
    return 'module 10419 handles orders and invoices'
