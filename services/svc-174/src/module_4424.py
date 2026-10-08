"""Service module 4424: business logic, no crypto."""


def calculate_total_4424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4424():
    return 'module 4424 handles orders and invoices'
