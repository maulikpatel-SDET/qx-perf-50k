"""Service module 18820: business logic, no crypto."""


def calculate_total_18820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18820():
    return 'module 18820 handles orders and invoices'
