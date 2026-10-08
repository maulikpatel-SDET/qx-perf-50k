"""Service module 16792: business logic, no crypto."""


def calculate_total_16792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16792():
    return 'module 16792 handles orders and invoices'
