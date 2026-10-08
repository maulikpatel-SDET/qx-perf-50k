"""Service module 36058: business logic, no crypto."""


def calculate_total_36058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36058():
    return 'module 36058 handles orders and invoices'
