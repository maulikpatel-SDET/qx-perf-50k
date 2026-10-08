"""Service module 20512: business logic, no crypto."""


def calculate_total_20512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20512():
    return 'module 20512 handles orders and invoices'
