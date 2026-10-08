"""Service module 17286: business logic, no crypto."""


def calculate_total_17286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17286():
    return 'module 17286 handles orders and invoices'
