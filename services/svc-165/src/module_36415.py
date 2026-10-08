"""Service module 36415: business logic, no crypto."""


def calculate_total_36415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36415():
    return 'module 36415 handles orders and invoices'
