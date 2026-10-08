"""Service module 39288: business logic, no crypto."""


def calculate_total_39288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39288():
    return 'module 39288 handles orders and invoices'
