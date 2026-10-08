"""Service module 91: business logic, no crypto."""


def calculate_total_91(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_91():
    return 'module 91 handles orders and invoices'
