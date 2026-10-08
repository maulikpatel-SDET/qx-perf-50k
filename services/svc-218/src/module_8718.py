"""Service module 8718: business logic, no crypto."""


def calculate_total_8718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8718():
    return 'module 8718 handles orders and invoices'
