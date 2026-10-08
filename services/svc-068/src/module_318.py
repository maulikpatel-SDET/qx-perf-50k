"""Service module 318: business logic, no crypto."""


def calculate_total_318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_318():
    return 'module 318 handles orders and invoices'
