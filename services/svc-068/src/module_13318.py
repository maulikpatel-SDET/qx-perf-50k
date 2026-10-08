"""Service module 13318: business logic, no crypto."""


def calculate_total_13318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13318():
    return 'module 13318 handles orders and invoices'
