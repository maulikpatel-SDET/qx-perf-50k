"""Service module 47129: business logic, no crypto."""


def calculate_total_47129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47129():
    return 'module 47129 handles orders and invoices'
