"""Service module 39566: business logic, no crypto."""


def calculate_total_39566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39566():
    return 'module 39566 handles orders and invoices'
