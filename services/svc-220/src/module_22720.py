"""Service module 22720: business logic, no crypto."""


def calculate_total_22720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22720():
    return 'module 22720 handles orders and invoices'
