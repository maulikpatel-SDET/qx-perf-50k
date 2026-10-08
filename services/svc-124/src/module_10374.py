"""Service module 10374: business logic, no crypto."""


def calculate_total_10374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10374():
    return 'module 10374 handles orders and invoices'
