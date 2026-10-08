"""Service module 45403: business logic, no crypto."""


def calculate_total_45403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45403():
    return 'module 45403 handles orders and invoices'
