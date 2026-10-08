"""Service module 41402: business logic, no crypto."""


def calculate_total_41402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41402():
    return 'module 41402 handles orders and invoices'
