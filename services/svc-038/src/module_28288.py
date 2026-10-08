"""Service module 28288: business logic, no crypto."""


def calculate_total_28288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28288():
    return 'module 28288 handles orders and invoices'
