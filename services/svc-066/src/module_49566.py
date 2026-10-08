"""Service module 49566: business logic, no crypto."""


def calculate_total_49566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49566():
    return 'module 49566 handles orders and invoices'
