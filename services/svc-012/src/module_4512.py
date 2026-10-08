"""Service module 4512: business logic, no crypto."""


def calculate_total_4512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4512():
    return 'module 4512 handles orders and invoices'
