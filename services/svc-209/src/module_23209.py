"""Service module 23209: business logic, no crypto."""


def calculate_total_23209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23209():
    return 'module 23209 handles orders and invoices'
