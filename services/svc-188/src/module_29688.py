"""Service module 29688: business logic, no crypto."""


def calculate_total_29688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29688():
    return 'module 29688 handles orders and invoices'
