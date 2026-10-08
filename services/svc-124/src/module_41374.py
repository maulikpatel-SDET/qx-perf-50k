"""Service module 41374: business logic, no crypto."""


def calculate_total_41374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41374():
    return 'module 41374 handles orders and invoices'
