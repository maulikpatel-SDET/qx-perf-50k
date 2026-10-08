"""Service module 41129: business logic, no crypto."""


def calculate_total_41129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41129():
    return 'module 41129 handles orders and invoices'
