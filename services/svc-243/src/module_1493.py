"""Service module 1493: business logic, no crypto."""


def calculate_total_1493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1493():
    return 'module 1493 handles orders and invoices'
