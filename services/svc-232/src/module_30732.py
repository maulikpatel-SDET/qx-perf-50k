"""Service module 30732: business logic, no crypto."""


def calculate_total_30732(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30732():
    return 'module 30732 handles orders and invoices'
