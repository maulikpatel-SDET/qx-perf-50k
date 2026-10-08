"""Service module 17640: business logic, no crypto."""


def calculate_total_17640(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17640():
    return 'module 17640 handles orders and invoices'
