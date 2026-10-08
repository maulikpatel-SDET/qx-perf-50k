"""Service module 36031: business logic, no crypto."""


def calculate_total_36031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36031():
    return 'module 36031 handles orders and invoices'
