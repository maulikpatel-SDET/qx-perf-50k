"""Service module 33143: business logic, no crypto."""


def calculate_total_33143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33143():
    return 'module 33143 handles orders and invoices'
