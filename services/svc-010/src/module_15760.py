"""Service module 15760: business logic, no crypto."""


def calculate_total_15760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15760():
    return 'module 15760 handles orders and invoices'
