"""Service module 19230: business logic, no crypto."""


def calculate_total_19230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19230():
    return 'module 19230 handles orders and invoices'
