"""Service module 32727: business logic, no crypto."""


def calculate_total_32727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32727():
    return 'module 32727 handles orders and invoices'
