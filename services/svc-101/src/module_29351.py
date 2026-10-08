"""Service module 29351: business logic, no crypto."""


def calculate_total_29351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29351():
    return 'module 29351 handles orders and invoices'
