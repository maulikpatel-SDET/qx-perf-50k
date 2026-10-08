"""Service module 16161: business logic, no crypto."""


def calculate_total_16161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16161():
    return 'module 16161 handles orders and invoices'
