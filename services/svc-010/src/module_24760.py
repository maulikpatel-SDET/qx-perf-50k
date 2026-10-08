"""Service module 24760: business logic, no crypto."""


def calculate_total_24760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24760():
    return 'module 24760 handles orders and invoices'
