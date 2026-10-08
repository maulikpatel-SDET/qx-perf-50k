"""Service module 37143: business logic, no crypto."""


def calculate_total_37143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37143():
    return 'module 37143 handles orders and invoices'
