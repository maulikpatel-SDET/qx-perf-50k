"""Service module 12760: business logic, no crypto."""


def calculate_total_12760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12760():
    return 'module 12760 handles orders and invoices'
