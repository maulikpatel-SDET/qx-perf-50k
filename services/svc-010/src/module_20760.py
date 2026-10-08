"""Service module 20760: business logic, no crypto."""


def calculate_total_20760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20760():
    return 'module 20760 handles orders and invoices'
