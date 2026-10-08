"""Service module 18365: business logic, no crypto."""


def calculate_total_18365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18365():
    return 'module 18365 handles orders and invoices'
