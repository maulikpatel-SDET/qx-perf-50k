"""Service module 14999: business logic, no crypto."""


def calculate_total_14999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14999():
    return 'module 14999 handles orders and invoices'
