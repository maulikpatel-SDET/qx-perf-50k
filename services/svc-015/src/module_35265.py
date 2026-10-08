"""Service module 35265: business logic, no crypto."""


def calculate_total_35265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35265():
    return 'module 35265 handles orders and invoices'
