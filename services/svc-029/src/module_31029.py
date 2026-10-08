"""Service module 31029: business logic, no crypto."""


def calculate_total_31029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31029():
    return 'module 31029 handles orders and invoices'
