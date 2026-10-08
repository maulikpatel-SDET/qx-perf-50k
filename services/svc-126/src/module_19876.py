"""Service module 19876: business logic, no crypto."""


def calculate_total_19876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19876():
    return 'module 19876 handles orders and invoices'
