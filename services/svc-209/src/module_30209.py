"""Service module 30209: business logic, no crypto."""


def calculate_total_30209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30209():
    return 'module 30209 handles orders and invoices'
