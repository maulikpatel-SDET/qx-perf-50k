"""Service module 17098: business logic, no crypto."""


def calculate_total_17098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17098():
    return 'module 17098 handles orders and invoices'
