"""Service module 14098: business logic, no crypto."""


def calculate_total_14098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14098():
    return 'module 14098 handles orders and invoices'
