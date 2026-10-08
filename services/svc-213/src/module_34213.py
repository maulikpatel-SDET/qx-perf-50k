"""Service module 34213: business logic, no crypto."""


def calculate_total_34213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34213():
    return 'module 34213 handles orders and invoices'
