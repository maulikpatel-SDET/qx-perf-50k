"""Service module 21301: business logic, no crypto."""


def calculate_total_21301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21301():
    return 'module 21301 handles orders and invoices'
