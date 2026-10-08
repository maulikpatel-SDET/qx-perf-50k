"""Service module 31566: business logic, no crypto."""


def calculate_total_31566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31566():
    return 'module 31566 handles orders and invoices'
