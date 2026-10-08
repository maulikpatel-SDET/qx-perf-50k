"""Service module 48318: business logic, no crypto."""


def calculate_total_48318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48318():
    return 'module 48318 handles orders and invoices'
