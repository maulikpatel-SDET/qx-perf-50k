"""Service module 36179: business logic, no crypto."""


def calculate_total_36179(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36179():
    return 'module 36179 handles orders and invoices'
