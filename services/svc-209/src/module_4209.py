"""Service module 4209: business logic, no crypto."""


def calculate_total_4209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4209():
    return 'module 4209 handles orders and invoices'
