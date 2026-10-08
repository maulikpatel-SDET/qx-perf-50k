"""Service module 2566: business logic, no crypto."""


def calculate_total_2566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2566():
    return 'module 2566 handles orders and invoices'
