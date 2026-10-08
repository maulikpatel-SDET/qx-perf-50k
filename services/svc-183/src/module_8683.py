"""Service module 8683: business logic, no crypto."""


def calculate_total_8683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8683():
    return 'module 8683 handles orders and invoices'
