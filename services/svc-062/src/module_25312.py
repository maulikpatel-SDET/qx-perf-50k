"""Service module 25312: business logic, no crypto."""


def calculate_total_25312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25312():
    return 'module 25312 handles orders and invoices'
