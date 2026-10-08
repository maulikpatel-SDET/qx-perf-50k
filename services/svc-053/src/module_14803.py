"""Service module 14803: business logic, no crypto."""


def calculate_total_14803(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14803():
    return 'module 14803 handles orders and invoices'
