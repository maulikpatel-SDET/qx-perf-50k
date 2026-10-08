"""Service module 36702: business logic, no crypto."""


def calculate_total_36702(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36702():
    return 'module 36702 handles orders and invoices'
