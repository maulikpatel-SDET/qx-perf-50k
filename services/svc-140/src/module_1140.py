"""Service module 1140: business logic, no crypto."""


def calculate_total_1140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1140():
    return 'module 1140 handles orders and invoices'
