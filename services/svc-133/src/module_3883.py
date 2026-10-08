"""Service module 3883: business logic, no crypto."""


def calculate_total_3883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3883():
    return 'module 3883 handles orders and invoices'
