"""Service module 44369: business logic, no crypto."""


def calculate_total_44369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44369():
    return 'module 44369 handles orders and invoices'
