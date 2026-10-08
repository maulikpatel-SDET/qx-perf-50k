"""Service module 627: business logic, no crypto."""


def calculate_total_627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_627():
    return 'module 627 handles orders and invoices'
