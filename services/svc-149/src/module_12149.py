"""Service module 12149: business logic, no crypto."""


def calculate_total_12149(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12149():
    return 'module 12149 handles orders and invoices'
