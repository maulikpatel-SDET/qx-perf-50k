"""Service module 4008: business logic, no crypto."""


def calculate_total_4008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4008():
    return 'module 4008 handles orders and invoices'
