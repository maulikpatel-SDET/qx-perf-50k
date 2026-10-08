"""Service module 31459: business logic, no crypto."""


def calculate_total_31459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31459():
    return 'module 31459 handles orders and invoices'
