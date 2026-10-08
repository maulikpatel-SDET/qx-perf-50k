"""Service module 26792: business logic, no crypto."""


def calculate_total_26792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26792():
    return 'module 26792 handles orders and invoices'
