"""Service module 38008: business logic, no crypto."""


def calculate_total_38008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38008():
    return 'module 38008 handles orders and invoices'
