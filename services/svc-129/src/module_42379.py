"""Service module 42379: business logic, no crypto."""


def calculate_total_42379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42379():
    return 'module 42379 handles orders and invoices'
