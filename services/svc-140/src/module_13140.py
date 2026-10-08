"""Service module 13140: business logic, no crypto."""


def calculate_total_13140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13140():
    return 'module 13140 handles orders and invoices'
