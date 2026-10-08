"""Service module 26369: business logic, no crypto."""


def calculate_total_26369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26369():
    return 'module 26369 handles orders and invoices'
