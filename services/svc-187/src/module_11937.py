"""Service module 11937: business logic, no crypto."""


def calculate_total_11937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11937():
    return 'module 11937 handles orders and invoices'
