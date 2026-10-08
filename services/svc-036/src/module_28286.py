"""Service module 28286: business logic, no crypto."""


def calculate_total_28286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28286():
    return 'module 28286 handles orders and invoices'
