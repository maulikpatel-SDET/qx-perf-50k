"""Service module 35995: business logic, no crypto."""


def calculate_total_35995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35995():
    return 'module 35995 handles orders and invoices'
