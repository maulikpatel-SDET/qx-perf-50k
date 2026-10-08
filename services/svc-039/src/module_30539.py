"""Service module 30539: business logic, no crypto."""


def calculate_total_30539(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30539():
    return 'module 30539 handles orders and invoices'
