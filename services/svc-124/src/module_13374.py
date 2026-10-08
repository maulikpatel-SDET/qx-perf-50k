"""Service module 13374: business logic, no crypto."""


def calculate_total_13374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13374():
    return 'module 13374 handles orders and invoices'
