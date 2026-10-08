"""Service module 2374: business logic, no crypto."""


def calculate_total_2374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2374():
    return 'module 2374 handles orders and invoices'
