"""Service module 28712: business logic, no crypto."""


def calculate_total_28712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28712():
    return 'module 28712 handles orders and invoices'
