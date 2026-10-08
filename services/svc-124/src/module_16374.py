"""Service module 16374: business logic, no crypto."""


def calculate_total_16374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16374():
    return 'module 16374 handles orders and invoices'
