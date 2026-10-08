"""Service module 36068: business logic, no crypto."""


def calculate_total_36068(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36068():
    return 'module 36068 handles orders and invoices'
