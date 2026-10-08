"""Service module 4312: business logic, no crypto."""


def calculate_total_4312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4312():
    return 'module 4312 handles orders and invoices'
