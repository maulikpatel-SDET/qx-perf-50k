"""Service module 25301: business logic, no crypto."""


def calculate_total_25301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25301():
    return 'module 25301 handles orders and invoices'
