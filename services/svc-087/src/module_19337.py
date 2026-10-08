"""Service module 19337: business logic, no crypto."""


def calculate_total_19337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19337():
    return 'module 19337 handles orders and invoices'
