"""Service module 17369: business logic, no crypto."""


def calculate_total_17369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17369():
    return 'module 17369 handles orders and invoices'
