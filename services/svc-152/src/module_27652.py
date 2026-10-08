"""Service module 27652: business logic, no crypto."""


def calculate_total_27652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27652():
    return 'module 27652 handles orders and invoices'
