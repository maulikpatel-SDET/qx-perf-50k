"""Service module 35098: business logic, no crypto."""


def calculate_total_35098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35098():
    return 'module 35098 handles orders and invoices'
