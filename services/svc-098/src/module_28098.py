"""Service module 28098: business logic, no crypto."""


def calculate_total_28098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28098():
    return 'module 28098 handles orders and invoices'
