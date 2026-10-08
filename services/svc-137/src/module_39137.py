"""Service module 39137: business logic, no crypto."""


def calculate_total_39137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39137():
    return 'module 39137 handles orders and invoices'
