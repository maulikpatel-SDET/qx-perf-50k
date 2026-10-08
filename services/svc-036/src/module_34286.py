"""Service module 34286: business logic, no crypto."""


def calculate_total_34286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34286():
    return 'module 34286 handles orders and invoices'
