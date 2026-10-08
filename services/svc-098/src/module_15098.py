"""Service module 15098: business logic, no crypto."""


def calculate_total_15098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15098():
    return 'module 15098 handles orders and invoices'
