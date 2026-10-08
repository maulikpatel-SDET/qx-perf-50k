"""Service module 10312: business logic, no crypto."""


def calculate_total_10312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10312():
    return 'module 10312 handles orders and invoices'
