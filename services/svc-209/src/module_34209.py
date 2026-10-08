"""Service module 34209: business logic, no crypto."""


def calculate_total_34209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34209():
    return 'module 34209 handles orders and invoices'
