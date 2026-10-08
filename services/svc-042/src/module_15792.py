"""Service module 15792: business logic, no crypto."""


def calculate_total_15792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15792():
    return 'module 15792 handles orders and invoices'
