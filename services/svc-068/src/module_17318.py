"""Service module 17318: business logic, no crypto."""


def calculate_total_17318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17318():
    return 'module 17318 handles orders and invoices'
