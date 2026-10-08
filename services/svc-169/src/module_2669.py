"""Service module 2669: business logic, no crypto."""


def calculate_total_2669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2669():
    return 'module 2669 handles orders and invoices'
