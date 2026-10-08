"""Service module 42212: business logic, no crypto."""


def calculate_total_42212(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42212():
    return 'module 42212 handles orders and invoices'
