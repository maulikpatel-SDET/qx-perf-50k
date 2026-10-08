"""Service module 29735: business logic, no crypto."""


def calculate_total_29735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29735():
    return 'module 29735 handles orders and invoices'
