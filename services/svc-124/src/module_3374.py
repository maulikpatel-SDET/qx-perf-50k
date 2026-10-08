"""Service module 3374: business logic, no crypto."""


def calculate_total_3374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3374():
    return 'module 3374 handles orders and invoices'
