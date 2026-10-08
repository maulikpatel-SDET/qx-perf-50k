"""Service module 8318: business logic, no crypto."""


def calculate_total_8318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8318():
    return 'module 8318 handles orders and invoices'
