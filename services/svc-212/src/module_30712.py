"""Service module 30712: business logic, no crypto."""


def calculate_total_30712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30712():
    return 'module 30712 handles orders and invoices'
