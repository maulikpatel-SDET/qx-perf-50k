"""Service module 25760: business logic, no crypto."""


def calculate_total_25760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25760():
    return 'module 25760 handles orders and invoices'
