"""Service module 46402: business logic, no crypto."""


def calculate_total_46402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46402():
    return 'module 46402 handles orders and invoices'
