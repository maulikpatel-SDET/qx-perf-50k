"""Service module 9820: business logic, no crypto."""


def calculate_total_9820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9820():
    return 'module 9820 handles orders and invoices'
