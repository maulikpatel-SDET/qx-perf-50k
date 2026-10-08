"""Service module 41566: business logic, no crypto."""


def calculate_total_41566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41566():
    return 'module 41566 handles orders and invoices'
