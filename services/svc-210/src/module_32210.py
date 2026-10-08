"""Service module 32210: business logic, no crypto."""


def calculate_total_32210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32210():
    return 'module 32210 handles orders and invoices'
