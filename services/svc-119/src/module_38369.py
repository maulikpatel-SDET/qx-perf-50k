"""Service module 38369: business logic, no crypto."""


def calculate_total_38369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38369():
    return 'module 38369 handles orders and invoices'
