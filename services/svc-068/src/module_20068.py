"""Service module 20068: business logic, no crypto."""


def calculate_total_20068(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20068():
    return 'module 20068 handles orders and invoices'
