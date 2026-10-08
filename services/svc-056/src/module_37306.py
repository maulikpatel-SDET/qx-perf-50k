"""Service module 37306: business logic, no crypto."""


def calculate_total_37306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37306():
    return 'module 37306 handles orders and invoices'
