"""Service module 28646: business logic, no crypto."""


def calculate_total_28646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28646():
    return 'module 28646 handles orders and invoices'
