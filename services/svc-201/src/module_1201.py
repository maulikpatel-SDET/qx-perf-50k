"""Service module 1201: business logic, no crypto."""


def calculate_total_1201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1201():
    return 'module 1201 handles orders and invoices'
