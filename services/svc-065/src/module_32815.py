"""Service module 32815: business logic, no crypto."""


def calculate_total_32815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32815():
    return 'module 32815 handles orders and invoices'
