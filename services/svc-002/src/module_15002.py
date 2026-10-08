"""Service module 15002: business logic, no crypto."""


def calculate_total_15002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15002():
    return 'module 15002 handles orders and invoices'
