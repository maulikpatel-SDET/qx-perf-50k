"""Service module 37696: business logic, no crypto."""


def calculate_total_37696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37696():
    return 'module 37696 handles orders and invoices'
