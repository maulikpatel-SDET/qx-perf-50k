"""Service module 15221: business logic, no crypto."""


def calculate_total_15221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15221():
    return 'module 15221 handles orders and invoices'
