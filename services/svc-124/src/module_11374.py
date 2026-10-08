"""Service module 11374: business logic, no crypto."""


def calculate_total_11374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11374():
    return 'module 11374 handles orders and invoices'
