"""Service module 23553: business logic, no crypto."""


def calculate_total_23553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23553():
    return 'module 23553 handles orders and invoices'
