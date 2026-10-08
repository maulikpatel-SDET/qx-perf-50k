"""Service module 16747: business logic, no crypto."""


def calculate_total_16747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16747():
    return 'module 16747 handles orders and invoices'
