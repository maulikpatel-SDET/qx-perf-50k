"""Service module 15306: business logic, no crypto."""


def calculate_total_15306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15306():
    return 'module 15306 handles orders and invoices'
