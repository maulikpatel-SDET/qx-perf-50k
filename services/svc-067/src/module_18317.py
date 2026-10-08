"""Service module 18317: business logic, no crypto."""


def calculate_total_18317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18317():
    return 'module 18317 handles orders and invoices'
