"""Service module 49129: business logic, no crypto."""


def calculate_total_49129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49129():
    return 'module 49129 handles orders and invoices'
