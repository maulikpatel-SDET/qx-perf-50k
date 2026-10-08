"""Service module 17820: business logic, no crypto."""


def calculate_total_17820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17820():
    return 'module 17820 handles orders and invoices'
