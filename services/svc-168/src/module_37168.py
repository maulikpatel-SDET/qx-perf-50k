"""Service module 37168: business logic, no crypto."""


def calculate_total_37168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37168():
    return 'module 37168 handles orders and invoices'
