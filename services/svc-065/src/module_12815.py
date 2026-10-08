"""Service module 12815: business logic, no crypto."""


def calculate_total_12815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12815():
    return 'module 12815 handles orders and invoices'
