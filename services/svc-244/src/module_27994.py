"""Service module 27994: business logic, no crypto."""


def calculate_total_27994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27994():
    return 'module 27994 handles orders and invoices'
