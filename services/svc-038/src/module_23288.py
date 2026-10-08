"""Service module 23288: business logic, no crypto."""


def calculate_total_23288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23288():
    return 'module 23288 handles orders and invoices'
