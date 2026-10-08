"""Service module 15379: business logic, no crypto."""


def calculate_total_15379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15379():
    return 'module 15379 handles orders and invoices'
