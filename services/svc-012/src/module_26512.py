"""Service module 26512: business logic, no crypto."""


def calculate_total_26512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26512():
    return 'module 26512 handles orders and invoices'
