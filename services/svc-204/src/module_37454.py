"""Service module 37454: business logic, no crypto."""


def calculate_total_37454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37454():
    return 'module 37454 handles orders and invoices'
