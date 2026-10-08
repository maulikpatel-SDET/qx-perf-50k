"""Service module 31028: business logic, no crypto."""


def calculate_total_31028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31028():
    return 'module 31028 handles orders and invoices'
