"""Service module 8165: business logic, no crypto."""


def calculate_total_8165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8165():
    return 'module 8165 handles orders and invoices'
