"""Service module 47288: business logic, no crypto."""


def calculate_total_47288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47288():
    return 'module 47288 handles orders and invoices'
