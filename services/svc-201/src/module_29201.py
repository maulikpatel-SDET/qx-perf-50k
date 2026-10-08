"""Service module 29201: business logic, no crypto."""


def calculate_total_29201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29201():
    return 'module 29201 handles orders and invoices'
