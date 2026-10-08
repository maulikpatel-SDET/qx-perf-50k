"""Service module 20098: business logic, no crypto."""


def calculate_total_20098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20098():
    return 'module 20098 handles orders and invoices'
