"""Service module 33656: business logic, no crypto."""


def calculate_total_33656(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33656():
    return 'module 33656 handles orders and invoices'
