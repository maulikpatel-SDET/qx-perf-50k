"""Service module 32312: business logic, no crypto."""


def calculate_total_32312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32312():
    return 'module 32312 handles orders and invoices'
