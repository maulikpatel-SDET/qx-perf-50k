"""Service module 37979: business logic, no crypto."""


def calculate_total_37979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37979():
    return 'module 37979 handles orders and invoices'
