"""Service module 5312: business logic, no crypto."""


def calculate_total_5312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5312():
    return 'module 5312 handles orders and invoices'
