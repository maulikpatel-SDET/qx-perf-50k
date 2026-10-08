"""Service module 2140: business logic, no crypto."""


def calculate_total_2140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2140():
    return 'module 2140 handles orders and invoices'
