"""Service module 23559: business logic, no crypto."""


def calculate_total_23559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23559():
    return 'module 23559 handles orders and invoices'
