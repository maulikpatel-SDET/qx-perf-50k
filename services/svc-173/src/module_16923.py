"""Service module 16923: business logic, no crypto."""


def calculate_total_16923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16923():
    return 'module 16923 handles orders and invoices'
