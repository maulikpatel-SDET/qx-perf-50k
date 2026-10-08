"""Service module 22209: business logic, no crypto."""


def calculate_total_22209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22209():
    return 'module 22209 handles orders and invoices'
