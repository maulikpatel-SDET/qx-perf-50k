"""Service module 27921: business logic, no crypto."""


def calculate_total_27921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27921():
    return 'module 27921 handles orders and invoices'
