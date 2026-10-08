"""Service module 30150: business logic, no crypto."""


def calculate_total_30150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30150():
    return 'module 30150 handles orders and invoices'
