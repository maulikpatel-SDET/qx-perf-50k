"""Service module 16381: business logic, no crypto."""


def calculate_total_16381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16381():
    return 'module 16381 handles orders and invoices'
