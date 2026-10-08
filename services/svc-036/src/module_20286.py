"""Service module 20286: business logic, no crypto."""


def calculate_total_20286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20286():
    return 'module 20286 handles orders and invoices'
