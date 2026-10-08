"""Service module 45209: business logic, no crypto."""


def calculate_total_45209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45209():
    return 'module 45209 handles orders and invoices'
