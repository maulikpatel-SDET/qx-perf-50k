"""Service module 18318: business logic, no crypto."""


def calculate_total_18318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18318():
    return 'module 18318 handles orders and invoices'
