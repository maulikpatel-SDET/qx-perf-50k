"""Service module 37693: business logic, no crypto."""


def calculate_total_37693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37693():
    return 'module 37693 handles orders and invoices'
