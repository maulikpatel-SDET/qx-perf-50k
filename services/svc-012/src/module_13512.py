"""Service module 13512: business logic, no crypto."""


def calculate_total_13512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13512():
    return 'module 13512 handles orders and invoices'
