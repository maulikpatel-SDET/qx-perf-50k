"""Service module 8369: business logic, no crypto."""


def calculate_total_8369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8369():
    return 'module 8369 handles orders and invoices'
