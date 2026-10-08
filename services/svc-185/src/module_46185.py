"""Service module 46185: business logic, no crypto."""


def calculate_total_46185(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46185():
    return 'module 46185 handles orders and invoices'
