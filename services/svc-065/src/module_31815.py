"""Service module 31815: business logic, no crypto."""


def calculate_total_31815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31815():
    return 'module 31815 handles orders and invoices'
