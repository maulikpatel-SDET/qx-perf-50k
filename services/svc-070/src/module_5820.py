"""Service module 5820: business logic, no crypto."""


def calculate_total_5820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5820():
    return 'module 5820 handles orders and invoices'
