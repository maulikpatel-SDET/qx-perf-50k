"""Service module 33806: business logic, no crypto."""


def calculate_total_33806(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33806():
    return 'module 33806 handles orders and invoices'
