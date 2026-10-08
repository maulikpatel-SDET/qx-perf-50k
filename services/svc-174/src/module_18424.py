"""Service module 18424: business logic, no crypto."""


def calculate_total_18424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18424():
    return 'module 18424 handles orders and invoices'
