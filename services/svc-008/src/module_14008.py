"""Service module 14008: business logic, no crypto."""


def calculate_total_14008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14008():
    return 'module 14008 handles orders and invoices'
