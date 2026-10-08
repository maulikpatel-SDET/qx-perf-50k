"""Service module 29760: business logic, no crypto."""


def calculate_total_29760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29760():
    return 'module 29760 handles orders and invoices'
