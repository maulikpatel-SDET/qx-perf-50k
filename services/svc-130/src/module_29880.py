"""Service module 29880: business logic, no crypto."""


def calculate_total_29880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29880():
    return 'module 29880 handles orders and invoices'
