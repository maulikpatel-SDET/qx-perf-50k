"""Service module 27864: business logic, no crypto."""


def calculate_total_27864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27864():
    return 'module 27864 handles orders and invoices'
