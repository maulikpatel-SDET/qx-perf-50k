"""Service module 35566: business logic, no crypto."""


def calculate_total_35566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35566():
    return 'module 35566 handles orders and invoices'
