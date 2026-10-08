"""Service module 140: business logic, no crypto."""


def calculate_total_140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_140():
    return 'module 140 handles orders and invoices'
