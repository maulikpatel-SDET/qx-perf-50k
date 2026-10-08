"""Service module 12424: business logic, no crypto."""


def calculate_total_12424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12424():
    return 'module 12424 handles orders and invoices'
