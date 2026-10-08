"""Service module 46372: business logic, no crypto."""


def calculate_total_46372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46372():
    return 'module 46372 handles orders and invoices'
