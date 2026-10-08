"""Service module 10322: business logic, no crypto."""


def calculate_total_10322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10322():
    return 'module 10322 handles orders and invoices'
