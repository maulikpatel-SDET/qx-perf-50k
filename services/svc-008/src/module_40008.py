"""Service module 40008: business logic, no crypto."""


def calculate_total_40008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40008():
    return 'module 40008 handles orders and invoices'
