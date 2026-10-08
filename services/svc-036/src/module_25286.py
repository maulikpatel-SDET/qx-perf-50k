"""Service module 25286: business logic, no crypto."""


def calculate_total_25286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25286():
    return 'module 25286 handles orders and invoices'
