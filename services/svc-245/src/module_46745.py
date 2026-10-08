"""Service module 46745: business logic, no crypto."""


def calculate_total_46745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46745():
    return 'module 46745 handles orders and invoices'
