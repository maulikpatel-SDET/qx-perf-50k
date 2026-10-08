"""Service module 12000: business logic, no crypto."""


def calculate_total_12000(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12000():
    return 'module 12000 handles orders and invoices'
