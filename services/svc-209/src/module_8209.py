"""Service module 8209: business logic, no crypto."""


def calculate_total_8209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8209():
    return 'module 8209 handles orders and invoices'
