"""Service module 28627: business logic, no crypto."""


def calculate_total_28627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28627():
    return 'module 28627 handles orders and invoices'
