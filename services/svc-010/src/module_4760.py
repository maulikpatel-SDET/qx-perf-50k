"""Service module 4760: business logic, no crypto."""


def calculate_total_4760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4760():
    return 'module 4760 handles orders and invoices'
