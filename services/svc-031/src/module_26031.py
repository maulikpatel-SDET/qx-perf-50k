"""Service module 26031: business logic, no crypto."""


def calculate_total_26031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26031():
    return 'module 26031 handles orders and invoices'
