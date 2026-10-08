"""Service module 38402: business logic, no crypto."""


def calculate_total_38402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38402():
    return 'module 38402 handles orders and invoices'
