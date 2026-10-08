"""Service module 35820: business logic, no crypto."""


def calculate_total_35820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35820():
    return 'module 35820 handles orders and invoices'
