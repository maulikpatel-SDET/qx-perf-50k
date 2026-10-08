"""Service module 232: business logic, no crypto."""


def calculate_total_232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_232():
    return 'module 232 handles orders and invoices'
