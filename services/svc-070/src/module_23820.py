"""Service module 23820: business logic, no crypto."""


def calculate_total_23820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23820():
    return 'module 23820 handles orders and invoices'
