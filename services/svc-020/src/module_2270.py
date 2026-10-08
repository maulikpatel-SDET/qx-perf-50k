"""Service module 2270: business logic, no crypto."""


def calculate_total_2270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2270():
    return 'module 2270 handles orders and invoices'
