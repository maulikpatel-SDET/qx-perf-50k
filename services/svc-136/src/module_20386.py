"""Service module 20386: business logic, no crypto."""


def calculate_total_20386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20386():
    return 'module 20386 handles orders and invoices'
