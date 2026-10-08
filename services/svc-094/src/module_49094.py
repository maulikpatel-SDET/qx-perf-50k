"""Service module 49094: business logic, no crypto."""


def calculate_total_49094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49094():
    return 'module 49094 handles orders and invoices'
