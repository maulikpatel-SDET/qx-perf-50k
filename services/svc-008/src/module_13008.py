"""Service module 13008: business logic, no crypto."""


def calculate_total_13008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13008():
    return 'module 13008 handles orders and invoices'
