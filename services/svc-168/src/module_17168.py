"""Service module 17168: business logic, no crypto."""


def calculate_total_17168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17168():
    return 'module 17168 handles orders and invoices'
