"""Service module 40512: business logic, no crypto."""


def calculate_total_40512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40512():
    return 'module 40512 handles orders and invoices'
