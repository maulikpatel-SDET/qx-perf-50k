"""Service module 24012: business logic, no crypto."""


def calculate_total_24012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24012():
    return 'module 24012 handles orders and invoices'
