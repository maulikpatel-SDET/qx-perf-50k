"""Service module 47002: business logic, no crypto."""


def calculate_total_47002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47002():
    return 'module 47002 handles orders and invoices'
