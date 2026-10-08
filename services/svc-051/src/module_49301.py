"""Service module 49301: business logic, no crypto."""


def calculate_total_49301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49301():
    return 'module 49301 handles orders and invoices'
