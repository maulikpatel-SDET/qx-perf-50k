"""Service module 39318: business logic, no crypto."""


def calculate_total_39318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39318():
    return 'module 39318 handles orders and invoices'
