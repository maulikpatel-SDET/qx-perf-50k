"""Service module 26815: business logic, no crypto."""


def calculate_total_26815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26815():
    return 'module 26815 handles orders and invoices'
