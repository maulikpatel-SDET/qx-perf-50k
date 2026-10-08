"""Service module 36396: business logic, no crypto."""


def calculate_total_36396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36396():
    return 'module 36396 handles orders and invoices'
