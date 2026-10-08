"""Service module 47718: business logic, no crypto."""


def calculate_total_47718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47718():
    return 'module 47718 handles orders and invoices'
