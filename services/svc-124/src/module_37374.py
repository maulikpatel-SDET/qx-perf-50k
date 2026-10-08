"""Service module 37374: business logic, no crypto."""


def calculate_total_37374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37374():
    return 'module 37374 handles orders and invoices'
