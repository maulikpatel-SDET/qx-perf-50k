"""Service module 29118: business logic, no crypto."""


def calculate_total_29118(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29118():
    return 'module 29118 handles orders and invoices'
