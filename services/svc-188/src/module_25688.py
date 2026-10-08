"""Service module 25688: business logic, no crypto."""


def calculate_total_25688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25688():
    return 'module 25688 handles orders and invoices'
