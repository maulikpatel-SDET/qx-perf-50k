"""Service module 32317: business logic, no crypto."""


def calculate_total_32317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32317():
    return 'module 32317 handles orders and invoices'
