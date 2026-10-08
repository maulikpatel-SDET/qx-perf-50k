"""Service module 38640: business logic, no crypto."""


def calculate_total_38640(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38640():
    return 'module 38640 handles orders and invoices'
