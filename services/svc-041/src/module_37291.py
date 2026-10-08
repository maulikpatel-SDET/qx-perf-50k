"""Service module 37291: business logic, no crypto."""


def calculate_total_37291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37291():
    return 'module 37291 handles orders and invoices'
