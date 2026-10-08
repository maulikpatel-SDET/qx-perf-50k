"""Service module 37286: business logic, no crypto."""


def calculate_total_37286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37286():
    return 'module 37286 handles orders and invoices'
