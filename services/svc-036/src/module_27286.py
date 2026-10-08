"""Service module 27286: business logic, no crypto."""


def calculate_total_27286(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27286():
    return 'module 27286 handles orders and invoices'
