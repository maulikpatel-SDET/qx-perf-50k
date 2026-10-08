"""Service module 38330: business logic, no crypto."""


def calculate_total_38330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38330():
    return 'module 38330 handles orders and invoices'
