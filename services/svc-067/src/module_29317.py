"""Service module 29317: business logic, no crypto."""


def calculate_total_29317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29317():
    return 'module 29317 handles orders and invoices'
