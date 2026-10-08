"""Service module 26379: business logic, no crypto."""


def calculate_total_26379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26379():
    return 'module 26379 handles orders and invoices'
