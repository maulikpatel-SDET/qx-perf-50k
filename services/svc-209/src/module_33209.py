"""Service module 33209: business logic, no crypto."""


def calculate_total_33209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33209():
    return 'module 33209 handles orders and invoices'
