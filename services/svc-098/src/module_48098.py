"""Service module 48098: business logic, no crypto."""


def calculate_total_48098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48098():
    return 'module 48098 handles orders and invoices'
