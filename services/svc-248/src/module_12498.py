"""Service module 12498: business logic, no crypto."""


def calculate_total_12498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12498():
    return 'module 12498 handles orders and invoices'
