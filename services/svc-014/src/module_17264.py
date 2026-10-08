"""Service module 17264: business logic, no crypto."""


def calculate_total_17264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17264():
    return 'module 17264 handles orders and invoices'
