"""Service module 36137: business logic, no crypto."""


def calculate_total_36137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36137():
    return 'module 36137 handles orders and invoices'
