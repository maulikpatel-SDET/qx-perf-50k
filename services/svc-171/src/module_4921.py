"""Service module 4921: business logic, no crypto."""


def calculate_total_4921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4921():
    return 'module 4921 handles orders and invoices'
