"""Service module 46312: business logic, no crypto."""


def calculate_total_46312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46312():
    return 'module 46312 handles orders and invoices'
