"""Service module 7374: business logic, no crypto."""


def calculate_total_7374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7374():
    return 'module 7374 handles orders and invoices'
