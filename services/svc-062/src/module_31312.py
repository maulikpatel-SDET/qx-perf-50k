"""Service module 31312: business logic, no crypto."""


def calculate_total_31312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31312():
    return 'module 31312 handles orders and invoices'
