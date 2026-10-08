"""Service module 3641: business logic, no crypto."""


def calculate_total_3641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3641():
    return 'module 3641 handles orders and invoices'
