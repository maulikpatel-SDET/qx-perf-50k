"""Service module 4202: business logic, no crypto."""


def calculate_total_4202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4202():
    return 'module 4202 handles orders and invoices'
