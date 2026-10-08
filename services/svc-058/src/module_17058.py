"""Service module 17058: business logic, no crypto."""


def calculate_total_17058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17058():
    return 'module 17058 handles orders and invoices'
