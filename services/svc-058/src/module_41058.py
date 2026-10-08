"""Service module 41058: business logic, no crypto."""


def calculate_total_41058(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41058():
    return 'module 41058 handles orders and invoices'
