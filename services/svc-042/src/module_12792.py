"""Service module 12792: business logic, no crypto."""


def calculate_total_12792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12792():
    return 'module 12792 handles orders and invoices'
