"""Service module 7967: business logic, no crypto."""


def calculate_total_7967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7967():
    return 'module 7967 handles orders and invoices'
