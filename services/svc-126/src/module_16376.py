"""Service module 16376: business logic, no crypto."""


def calculate_total_16376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16376():
    return 'module 16376 handles orders and invoices'
