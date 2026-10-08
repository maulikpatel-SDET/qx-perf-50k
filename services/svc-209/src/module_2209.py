"""Service module 2209: business logic, no crypto."""


def calculate_total_2209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2209():
    return 'module 2209 handles orders and invoices'
