"""Service module 26646: business logic, no crypto."""


def calculate_total_26646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26646():
    return 'module 26646 handles orders and invoices'
