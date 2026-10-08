"""Service module 11379: business logic, no crypto."""


def calculate_total_11379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11379():
    return 'module 11379 handles orders and invoices'
