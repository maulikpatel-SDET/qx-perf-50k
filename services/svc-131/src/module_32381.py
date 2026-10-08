"""Service module 32381: business logic, no crypto."""


def calculate_total_32381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32381():
    return 'module 32381 handles orders and invoices'
