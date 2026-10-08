"""Service module 37937: business logic, no crypto."""


def calculate_total_37937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37937():
    return 'module 37937 handles orders and invoices'
