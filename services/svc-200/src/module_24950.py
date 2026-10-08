"""Service module 24950: business logic, no crypto."""


def calculate_total_24950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24950():
    return 'module 24950 handles orders and invoices'
