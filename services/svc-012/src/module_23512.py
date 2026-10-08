"""Service module 23512: business logic, no crypto."""


def calculate_total_23512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23512():
    return 'module 23512 handles orders and invoices'
