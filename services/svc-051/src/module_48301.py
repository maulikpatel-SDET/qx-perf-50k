"""Service module 48301: business logic, no crypto."""


def calculate_total_48301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48301():
    return 'module 48301 handles orders and invoices'
