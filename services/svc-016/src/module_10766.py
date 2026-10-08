"""Service module 10766: business logic, no crypto."""


def calculate_total_10766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10766():
    return 'module 10766 handles orders and invoices'
