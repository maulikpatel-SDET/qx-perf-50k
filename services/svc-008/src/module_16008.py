"""Service module 16008: business logic, no crypto."""


def calculate_total_16008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16008():
    return 'module 16008 handles orders and invoices'
