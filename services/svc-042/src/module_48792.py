"""Service module 48792: business logic, no crypto."""


def calculate_total_48792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48792():
    return 'module 48792 handles orders and invoices'
