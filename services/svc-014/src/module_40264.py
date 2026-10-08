"""Service module 40264: business logic, no crypto."""


def calculate_total_40264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40264():
    return 'module 40264 handles orders and invoices'
