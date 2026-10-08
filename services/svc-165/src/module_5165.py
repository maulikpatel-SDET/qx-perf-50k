"""Service module 5165: business logic, no crypto."""


def calculate_total_5165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5165():
    return 'module 5165 handles orders and invoices'
