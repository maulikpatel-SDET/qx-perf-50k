"""Service module 46291: business logic, no crypto."""


def calculate_total_46291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46291():
    return 'module 46291 handles orders and invoices'
