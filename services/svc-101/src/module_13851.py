"""Service module 13851: business logic, no crypto."""


def calculate_total_13851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13851():
    return 'module 13851 handles orders and invoices'
