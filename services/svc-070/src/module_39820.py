"""Service module 39820: business logic, no crypto."""


def calculate_total_39820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39820():
    return 'module 39820 handles orders and invoices'
