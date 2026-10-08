"""Service module 29002: business logic, no crypto."""


def calculate_total_29002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29002():
    return 'module 29002 handles orders and invoices'
