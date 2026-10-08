"""Service module 17301: business logic, no crypto."""


def calculate_total_17301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17301():
    return 'module 17301 handles orders and invoices'
