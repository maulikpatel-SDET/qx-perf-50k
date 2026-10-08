"""Service module 19374: business logic, no crypto."""


def calculate_total_19374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19374():
    return 'module 19374 handles orders and invoices'
