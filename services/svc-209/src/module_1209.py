"""Service module 1209: business logic, no crypto."""


def calculate_total_1209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1209():
    return 'module 1209 handles orders and invoices'
