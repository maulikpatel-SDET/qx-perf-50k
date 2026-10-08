"""Service module 46970: business logic, no crypto."""


def calculate_total_46970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46970():
    return 'module 46970 handles orders and invoices'
