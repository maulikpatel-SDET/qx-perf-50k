"""Service module 37369: business logic, no crypto."""


def calculate_total_37369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37369():
    return 'module 37369 handles orders and invoices'
