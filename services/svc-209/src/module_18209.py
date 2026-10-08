"""Service module 18209: business logic, no crypto."""


def calculate_total_18209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18209():
    return 'module 18209 handles orders and invoices'
