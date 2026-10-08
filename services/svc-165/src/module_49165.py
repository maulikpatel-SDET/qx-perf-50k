"""Service module 49165: business logic, no crypto."""


def calculate_total_49165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49165():
    return 'module 49165 handles orders and invoices'
