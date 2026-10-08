"""Service module 46732: business logic, no crypto."""


def calculate_total_46732(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46732():
    return 'module 46732 handles orders and invoices'
