"""Service module 4318: business logic, no crypto."""


def calculate_total_4318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4318():
    return 'module 4318 handles orders and invoices'
