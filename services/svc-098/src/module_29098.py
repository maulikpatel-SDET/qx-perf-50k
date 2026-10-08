"""Service module 29098: business logic, no crypto."""


def calculate_total_29098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29098():
    return 'module 29098 handles orders and invoices'
