"""Service module 24333: business logic, no crypto."""


def calculate_total_24333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24333():
    return 'module 24333 handles orders and invoices'
