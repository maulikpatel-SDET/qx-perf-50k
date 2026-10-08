"""Service module 41155: business logic, no crypto."""


def calculate_total_41155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41155():
    return 'module 41155 handles orders and invoices'
