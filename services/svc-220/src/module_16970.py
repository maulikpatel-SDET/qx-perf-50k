"""Service module 16970: business logic, no crypto."""


def calculate_total_16970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16970():
    return 'module 16970 handles orders and invoices'
