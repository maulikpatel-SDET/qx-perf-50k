"""Service module 41379: business logic, no crypto."""


def calculate_total_41379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41379():
    return 'module 41379 handles orders and invoices'
