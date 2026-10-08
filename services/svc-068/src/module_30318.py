"""Service module 30318: business logic, no crypto."""


def calculate_total_30318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30318():
    return 'module 30318 handles orders and invoices'
