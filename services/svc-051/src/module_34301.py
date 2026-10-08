"""Service module 34301: business logic, no crypto."""


def calculate_total_34301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34301():
    return 'module 34301 handles orders and invoices'
