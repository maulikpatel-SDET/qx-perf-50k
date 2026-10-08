"""Service module 39209: business logic, no crypto."""


def calculate_total_39209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39209():
    return 'module 39209 handles orders and invoices'
