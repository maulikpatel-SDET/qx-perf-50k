"""Service module 46424: business logic, no crypto."""


def calculate_total_46424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46424():
    return 'module 46424 handles orders and invoices'
