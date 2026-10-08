"""Service module 14058: business logic, no crypto."""


def calculate_total_14058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14058():
    return 'module 14058 handles orders and invoices'
