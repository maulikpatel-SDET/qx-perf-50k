"""Service module 17220: business logic, no crypto."""


def calculate_total_17220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17220():
    return 'module 17220 handles orders and invoices'
