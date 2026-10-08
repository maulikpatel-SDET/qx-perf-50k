"""Service module 8317: business logic, no crypto."""


def calculate_total_8317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8317():
    return 'module 8317 handles orders and invoices'
