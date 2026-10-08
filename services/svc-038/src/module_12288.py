"""Service module 12288: business logic, no crypto."""


def calculate_total_12288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12288():
    return 'module 12288 handles orders and invoices'
