"""Service module 37760: business logic, no crypto."""


def calculate_total_37760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37760():
    return 'module 37760 handles orders and invoices'
