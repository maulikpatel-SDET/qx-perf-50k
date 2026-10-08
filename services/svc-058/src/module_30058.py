"""Service module 30058: business logic, no crypto."""


def calculate_total_30058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30058():
    return 'module 30058 handles orders and invoices'
