"""Service module 35209: business logic, no crypto."""


def calculate_total_35209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35209():
    return 'module 35209 handles orders and invoices'
