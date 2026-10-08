"""Service module 45096: business logic, no crypto."""


def calculate_total_45096(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45096():
    return 'module 45096 handles orders and invoices'
