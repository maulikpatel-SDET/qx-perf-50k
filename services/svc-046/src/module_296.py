"""Service module 296: business logic, no crypto."""


def calculate_total_296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_296():
    return 'module 296 handles orders and invoices'
