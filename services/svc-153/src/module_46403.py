"""Service module 46403: business logic, no crypto."""


def calculate_total_46403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46403():
    return 'module 46403 handles orders and invoices'
