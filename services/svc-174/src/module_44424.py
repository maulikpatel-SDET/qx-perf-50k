"""Service module 44424: business logic, no crypto."""


def calculate_total_44424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44424():
    return 'module 44424 handles orders and invoices'
