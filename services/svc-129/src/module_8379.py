"""Service module 8379: business logic, no crypto."""


def calculate_total_8379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8379():
    return 'module 8379 handles orders and invoices'
