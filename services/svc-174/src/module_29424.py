"""Service module 29424: business logic, no crypto."""


def calculate_total_29424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29424():
    return 'module 29424 handles orders and invoices'
