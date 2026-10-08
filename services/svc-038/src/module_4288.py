"""Service module 4288: business logic, no crypto."""


def calculate_total_4288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4288():
    return 'module 4288 handles orders and invoices'
