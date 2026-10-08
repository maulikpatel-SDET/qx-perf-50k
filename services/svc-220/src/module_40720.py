"""Service module 40720: business logic, no crypto."""


def calculate_total_40720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40720():
    return 'module 40720 handles orders and invoices'
