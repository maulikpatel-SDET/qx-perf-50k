"""Service module 34318: business logic, no crypto."""


def calculate_total_34318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34318():
    return 'module 34318 handles orders and invoices'
