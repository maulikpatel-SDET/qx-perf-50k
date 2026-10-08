"""Service module 15286: business logic, no crypto."""


def calculate_total_15286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15286():
    return 'module 15286 handles orders and invoices'
