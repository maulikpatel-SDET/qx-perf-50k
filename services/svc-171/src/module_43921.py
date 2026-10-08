"""Service module 43921: business logic, no crypto."""


def calculate_total_43921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43921():
    return 'module 43921 handles orders and invoices'
