"""Service module 44533: business logic, no crypto."""


def calculate_total_44533(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44533():
    return 'module 44533 handles orders and invoices'
