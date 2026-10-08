"""Service module 37847: business logic, no crypto."""


def calculate_total_37847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37847():
    return 'module 37847 handles orders and invoices'
