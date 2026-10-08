"""Service module 15209: business logic, no crypto."""


def calculate_total_15209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15209():
    return 'module 15209 handles orders and invoices'
