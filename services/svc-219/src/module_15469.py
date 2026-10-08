"""Service module 15469: business logic, no crypto."""


def calculate_total_15469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15469():
    return 'module 15469 handles orders and invoices'
