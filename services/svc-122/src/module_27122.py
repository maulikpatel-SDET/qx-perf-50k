"""Service module 27122: business logic, no crypto."""


def calculate_total_27122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27122():
    return 'module 27122 handles orders and invoices'
