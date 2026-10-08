"""Service module 12100: business logic, no crypto."""


def calculate_total_12100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12100():
    return 'module 12100 handles orders and invoices'
