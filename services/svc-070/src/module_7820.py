"""Service module 7820: business logic, no crypto."""


def calculate_total_7820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7820():
    return 'module 7820 handles orders and invoices'
