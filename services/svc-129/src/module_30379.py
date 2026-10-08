"""Service module 30379: business logic, no crypto."""


def calculate_total_30379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30379():
    return 'module 30379 handles orders and invoices'
