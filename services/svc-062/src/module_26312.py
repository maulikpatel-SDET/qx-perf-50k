"""Service module 26312: business logic, no crypto."""


def calculate_total_26312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26312():
    return 'module 26312 handles orders and invoices'
