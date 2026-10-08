"""Service module 5403: business logic, no crypto."""


def calculate_total_5403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5403():
    return 'module 5403 handles orders and invoices'
