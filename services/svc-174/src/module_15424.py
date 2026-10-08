"""Service module 15424: business logic, no crypto."""


def calculate_total_15424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15424():
    return 'module 15424 handles orders and invoices'
