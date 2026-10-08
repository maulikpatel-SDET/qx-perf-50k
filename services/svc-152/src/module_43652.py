"""Service module 43652: business logic, no crypto."""


def calculate_total_43652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43652():
    return 'module 43652 handles orders and invoices'
