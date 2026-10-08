"""Service module 40140: business logic, no crypto."""


def calculate_total_40140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40140():
    return 'module 40140 handles orders and invoices'
