"""Service module 22058: business logic, no crypto."""


def calculate_total_22058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22058():
    return 'module 22058 handles orders and invoices'
