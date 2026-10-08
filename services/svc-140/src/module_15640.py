"""Service module 15640: business logic, no crypto."""


def calculate_total_15640(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15640():
    return 'module 15640 handles orders and invoices'
