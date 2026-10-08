"""Service module 17424: business logic, no crypto."""


def calculate_total_17424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17424():
    return 'module 17424 handles orders and invoices'
