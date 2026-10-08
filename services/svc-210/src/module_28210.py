"""Service module 28210: business logic, no crypto."""


def calculate_total_28210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28210():
    return 'module 28210 handles orders and invoices'
