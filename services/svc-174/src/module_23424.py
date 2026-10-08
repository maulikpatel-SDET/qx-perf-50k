"""Service module 23424: business logic, no crypto."""


def calculate_total_23424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23424():
    return 'module 23424 handles orders and invoices'
