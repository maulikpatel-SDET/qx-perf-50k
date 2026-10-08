"""Service module 23374: business logic, no crypto."""


def calculate_total_23374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23374():
    return 'module 23374 handles orders and invoices'
