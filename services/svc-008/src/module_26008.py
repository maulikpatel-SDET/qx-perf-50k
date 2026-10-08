"""Service module 26008: business logic, no crypto."""


def calculate_total_26008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26008():
    return 'module 26008 handles orders and invoices'
