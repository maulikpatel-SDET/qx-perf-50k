"""Service module 22288: business logic, no crypto."""


def calculate_total_22288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22288():
    return 'module 22288 handles orders and invoices'
