"""Service module 15058: business logic, no crypto."""


def calculate_total_15058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15058():
    return 'module 15058 handles orders and invoices'
