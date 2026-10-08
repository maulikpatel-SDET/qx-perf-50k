"""Service module 14606: business logic, no crypto."""


def calculate_total_14606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14606():
    return 'module 14606 handles orders and invoices'
