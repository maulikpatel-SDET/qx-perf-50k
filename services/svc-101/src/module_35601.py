"""Service module 35601: business logic, no crypto."""


def calculate_total_35601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35601():
    return 'module 35601 handles orders and invoices'
