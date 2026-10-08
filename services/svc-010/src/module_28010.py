"""Service module 28010: business logic, no crypto."""


def calculate_total_28010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28010():
    return 'module 28010 handles orders and invoices'
