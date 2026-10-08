"""Service module 12559: business logic, no crypto."""


def calculate_total_12559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12559():
    return 'module 12559 handles orders and invoices'
