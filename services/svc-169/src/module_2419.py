"""Service module 2419: business logic, no crypto."""


def calculate_total_2419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2419():
    return 'module 2419 handles orders and invoices'
