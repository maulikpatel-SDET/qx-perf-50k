"""Service module 41381: business logic, no crypto."""


def calculate_total_41381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41381():
    return 'module 41381 handles orders and invoices'
