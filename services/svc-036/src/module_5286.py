"""Service module 5286: business logic, no crypto."""


def calculate_total_5286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5286():
    return 'module 5286 handles orders and invoices'
