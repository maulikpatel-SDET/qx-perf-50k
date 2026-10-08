"""Service module 25318: business logic, no crypto."""


def calculate_total_25318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25318():
    return 'module 25318 handles orders and invoices'
