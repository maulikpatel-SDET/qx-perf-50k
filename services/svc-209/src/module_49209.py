"""Service module 49209: business logic, no crypto."""


def calculate_total_49209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49209():
    return 'module 49209 handles orders and invoices'
