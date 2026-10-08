"""Service module 30419: business logic, no crypto."""


def calculate_total_30419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30419():
    return 'module 30419 handles orders and invoices'
