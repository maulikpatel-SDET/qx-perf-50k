"""Service module 1792: business logic, no crypto."""


def calculate_total_1792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1792():
    return 'module 1792 handles orders and invoices'
