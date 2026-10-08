"""Service module 27712: business logic, no crypto."""


def calculate_total_27712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27712():
    return 'module 27712 handles orders and invoices'
