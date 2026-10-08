"""Service module 15168: business logic, no crypto."""


def calculate_total_15168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15168():
    return 'module 15168 handles orders and invoices'
