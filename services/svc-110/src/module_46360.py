"""Service module 46360: business logic, no crypto."""


def calculate_total_46360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46360():
    return 'module 46360 handles orders and invoices'
